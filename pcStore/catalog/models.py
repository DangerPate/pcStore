from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.utils import timezone
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


class Product(models.Model):
    # === ВАШИ СТАРЫЕ ПОЛЯ (сохранены + доработаны) ===
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

    # === НОВЫЕ ОБЯЗАТЕЛЬНЫЕ ПОЛЯ ===
    slug = models.SlugField('URL-метка', blank=True, db_index=True)
    sku = models.CharField('Артикул', max_length=50, unique=True, blank=True, null=True, db_index=True)
    description = models.TextField('Полное описание', blank=True)
    old_price = models.DecimalField('Старая цена', max_digits=10, decimal_places=2, blank=True, null=True,
                                    help_text='Заполните для отображения скидки')

    # === МАРКЕТИНГ И СТАТУСЫ ===
    is_active = models.BooleanField('Опубликован', default=True, db_index=True)
    is_new = models.BooleanField('Новинка', default=False, db_index=True)
    is_hit = models.BooleanField('Хит продаж', default=False, db_index=True)
    brand = models.CharField('Бренд / Производитель', max_length=100, blank=True, db_index=True)

    # === ТЕХНИЧЕСКИЕ / ЛОГИСТИЧЕСКИЕ ===
    weight = models.DecimalField('Вес (кг)', max_digits=6, decimal_places=2, blank=True, null=True)
    views = models.PositiveIntegerField('Просмотры', default=0, editable=False)

    # === АВТОДАТЫ ===
    created_at = models.DateTimeField('Дата создания', auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-created_at']  # Новые сверху по умолчанию
        indexes = [
            models.Index(fields=['slug']),
            models.Index(fields=['price']),
            models.Index(fields=['is_active', 'is_hit']),
            models.Index(fields=['brand']),
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

        # Автогенерация SKU (если не задан вручную)
        if not self.sku:
            self.sku = f"PRD-{timezone.now().strftime('%y%m%d')}-{random.randint(1000, 9999)}"

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        # Будет работать, когда создадите view для детальной страницы товара
        return reverse('product_detail', kwargs={'slug': self.slug})

    # === БИЗНЕС-ЛОГИКА (вызываются в шаблонах как product.price_with_discount) ===
    @property
    def price_with_discount(self):
        """Возвращает цену со скидкой, если старая цена задана и больше текущей"""
        if self.old_price and self.old_price > self.price:
            return self.price
        return None

    @property
    def discount_percent(self):
        """Процент скидки"""
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
            return 'Мало (осталось ' + str(self.in_stock) + ')'
        else:
            return 'Под заказ'