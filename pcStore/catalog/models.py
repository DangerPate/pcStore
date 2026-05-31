from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.utils import timezone
from django.conf import settings
import random

class Category(models.Model):
    title = models.CharField('Название', max_length=50)
    slug = models.SlugField('URL-метка', null=True, blank=True)  # 🔑 НОВОЕ ПОЛЕ
    icon = models.CharField('Иконка (Bootstrap)', max_length=50, default='bi-box', blank=True)
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Автозаполнение слага из title, если поле пустое
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=False)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Возвращает URL категории"""
        from django.urls import reverse
        return reverse('catalog:category', kwargs={'category_slug': self.slug})


# catalog/models.py

class Product(models.Model):
    # === БАЗОВЫЕ ПОЛЯ ===
    title = models.CharField('Название', max_length=150, db_index=True)
    info = models.TextField('Краткая информация / характеристики', blank=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    image = models.ImageField(
        'Основное изображение',
        upload_to='products/%Y/%m/%d/',
        blank=True, null=True
    )
    in_stock = models.PositiveIntegerField('Остаток на складе', default=0)
    warranty = models.CharField('Гарантия', max_length=50, default='12 месяцев', blank=True)
    categories = models.ManyToManyField('Category', blank=True, related_name='products', verbose_name='Категории')

    # === ИДЕНТИФИКАТОРЫ ===
    slug = models.SlugField('URL-метка', blank=True, db_index=True)
    sku = models.CharField('Артикул', max_length=50, unique=True, blank=True, null=True, db_index=True)
    description = models.TextField('Полное описание', blank=True)
    old_price = models.DecimalField('Старая цена', max_digits=10, decimal_places=2, blank=True, null=True,
                                    help_text='Заполните для отображения скидки')

    # === СТАТУСЫ ===
    is_active = models.BooleanField('Опубликован', default=True, db_index=True)
    brand = models.CharField('Бренд / Производитель', max_length=100, blank=True, db_index=True)

    # === 🔥 АВТО-МАРКЕРЫ (ручное переопределение возможно) ===
    # Для принудительного включения/выключения (опционально)
    force_hit = models.BooleanField('🔥 Принудительно хит', default=False, help_text='Игнорировать авто-расчёт')
    force_new = models.BooleanField('✨ Принудительно новинка', default=False, help_text='Игнорировать авто-расчёт')

    # === ТЕХНИЧЕСКИЕ ===
    weight = models.DecimalField('Вес (кг)', max_digits=6, decimal_places=2, blank=True, null=True)
    views = models.PositiveIntegerField('Просмотры', default=0, editable=False)
    specifications = models.JSONField('Характеристики', blank=True, null=True, default=dict)

    # === ДАТЫ ===
    created_at = models.DateTimeField('Дата создания', auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)

    # === НАСТРОЙКИ АВТО-МАРКЕРОВ ===
    NEW_PRODUCT_DAYS = 14  # 🔑 Товар считается новинкой первые 14 дней
    HIT_VIEWS_THRESHOLD = 500  # 🔑 Минимум просмотров для статуса "хит"
    HIT_TOP_PERCENT = 10  # 🔑 Или топ-10% товаров по просмотрам

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['slug']),
            models.Index(fields=['price']),
            models.Index(fields=['is_active', 'created_at']),
            models.Index(fields=['brand']),
            models.Index(fields=['-views']),  # 🔑 Для быстрых запросов по популярности
        ]

    def __str__(self):
        return f"{self.title} ({self.sku or 'Без артикула'})"

    def save(self, *args, **kwargs):
        # Автогенерация slug
        if not self.slug:
            base_slug = slugify(self.title, allow_unicode=False)
            slug = base_slug
            counter = 1
            while Product.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug

        # Автогенерация SKU
        if not self.sku:
            self.sku = f"PRD-{timezone.now().strftime('%y%m%d')}-{random.randint(1000, 9999)}"

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('catalog:product_detail', kwargs={'slug': self.slug})

    # 🔥 === АВТО-МАРКЕР: НОВИНКА ===
    @property
    def is_new(self):
        """Товар — новинка, если создан менее чем NEW_PRODUCT_DAYS дней назад"""
        if self.force_new:
            return True
        from django.utils import timezone
        from datetime import timedelta
        return timezone.now() - self.created_at < timedelta(days=self.NEW_PRODUCT_DAYS)

    @property
    def new_badge_days_left(self):
        """Сколько дней осталось до снятия статуса 'новинка'"""
        if not self.is_new:
            return 0
        from django.utils import timezone
        from datetime import timedelta
        end_date = self.created_at + timedelta(days=self.NEW_PRODUCT_DAYS)
        return (end_date - timezone.now()).days

    # 🔥 === АВТО-МАРКЕР: ХИТ ПРОДАЖ ===
    @property
    def is_hit(self):
        """
        Товар — хит, если:
        1. force_hit = True, ИЛИ
        2. Просмотры >= HIT_VIEWS_THRESHOLD, ИЛИ
        3. Товар входит в топ HIT_TOP_PERCENT% по просмотрам
        """
        if self.force_hit:
            return True

        # Простая проверка по порогу
        if self.views >= self.HIT_VIEWS_THRESHOLD:
            return True

        # Проверка по проценту (топ-10%)
        from django.db.models import Max
        max_views = Product.objects.filter(is_active=True).aggregate(max_v=Max('views'))['max_v'] or 1
        if max_views > 0 and self.views / max_views >= (1 - self.HIT_TOP_PERCENT / 100):
            return True

        return False

    @property
    def views_rank(self):
        """Место товара в рейтинге по просмотрам (1 = самый популярный)"""
        # 🔥 Оптимизация: кэшировать в продакшене
        return Product.objects.filter(
            is_active=True, views__gte=self.views
        ).count()

    # === БИЗНЕС-ЛОГИКА ===
    @property
    def price_with_discount(self):
        if self.old_price and self.old_price > self.price:
            return self.price
        return None

    @property
    def discount_percent(self):
        if self.old_price and self.old_price > self.price:
            return round(((self.old_price - self.price) / self.old_price) * 100)
        return 0

    @property
    def is_in_stock(self):
        return self.in_stock > 0

    @property
    def stock_status_label(self):
        if self.in_stock > 10:
            return 'В наличии'
        elif self.in_stock > 0:
            return f'Мало (осталось {self.in_stock})'
        else:
            return 'Под заказ'

    @property
    def review_count(self):
        """Заглушка: возвращает случайное число отзывов (10-500)"""
        # 🔥 В будущем: return self.reviews.count()
        return (self.id * 7 + 13) % 491 + 10  # Псевдо-рандом на основе ID
    # 🔥 === УВЕЛИЧЕНИЕ ПРОСМОТРОВ ===
    def increment_views(self):
        """Безопасное увеличение счётчика просмотров"""
        Product.objects.filter(pk=self.pk).update(views=models.F('views') + 1)
        self.views += 1  # Обновляем локально


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='catalog_reviews')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    author_name = models.CharField('Имя автора', max_length=100, blank=True)

    # 🔥 Рейтинг
    rating = models.PositiveSmallIntegerField('Оценка', choices=[(i, str(i)) for i in range(1, 6)])

    # 🔥 Новые поля
    pros = models.TextField('Достоинства', blank=True, help_text='Что понравилось?')
    cons = models.TextField('Недостатки', blank=True, help_text='Что не понравилось?')
    comment = models.TextField('Комментарий', help_text='Ваш подробный отзыв')

    # 🔥 Чекбокс проблемы
    has_issue = models.BooleanField('Есть проблема с описанием', default=False)
    issue_description = models.TextField('Описание проблемы', blank=True, help_text='Опишите, что не соответствует')

    is_verified_purchase = models.BooleanField('Проверенная покупка', default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return f"Отзыв на {self.product.title} от {self.author_name or self.user}"


class ReviewAttachment(models.Model):
    """Вложения к отзыву (фото/видео)"""
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='attachments')
    file = models.FileField('Файл', upload_to='reviews/%Y/%m/%d/')
    file_type = models.CharField('Тип', max_length=10, choices=[
        ('image', 'Изображение'),
        ('video', 'Видео')
    ])
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Вложение отзыва'
        verbose_name_plural = 'Вложения отзывов'

    def __str__(self):
        return f"Вложение для отзыва #{self.review.id}"

# catalog/models.py

class ReviewVote(models.Model):
    """Лайки и дизлайки отзывов"""
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='votes')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    vote = models.SmallIntegerField(choices=[(1, 'Like'), (-1, 'Dislike')])
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('review', 'user')
        verbose_name = 'Голос за отзыв'

    def __str__(self):
        return f"{'👍' if self.vote == 1 else '👎'} {self.user} для отзыва #{self.review.id}"


class ReviewComment(models.Model):
    """Комментарии под отзывами"""
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField('Текст комментария')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Комментарий к отзыву'

    def __str__(self):
        return f"Комментарий от {self.user} к отзыву #{self.review.id}"