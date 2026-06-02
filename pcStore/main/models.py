
from django.db import models
from catalog.models import Product, Category

class Banner(models.Model):
    """Модель промо-баннера для главной страницы"""

    image = models.ImageField('Изображение баннера', upload_to='banners/%Y/%m/%d/')
    overlay_color = models.CharField('Цвет наложения', max_length=30,
                                     default='rgba(0,0,0,0.3)',
                                     help_text='Прозрачное наложение на изображение (HEX или RGBA)')

    title = models.CharField('Заголовок', max_length=100, blank=True)
    subtitle = models.CharField('Подзаголовок', max_length=200, blank=True)
    description = models.TextField('Описание', blank=True)

    button_text = models.CharField('Текст кнопки', max_length=50,
                                   default='Подробнее', blank=True)
    button_color = models.CharField('Цвет кнопки', max_length=7,
                                    default='#ff6b00',
                                    help_text='HEX цвет (например, #ff6b00)')

    LINK_TYPES = [
        ('category', 'Категория'),
        ('product', 'Товар'),
        ('custom', 'Произвольный URL'),
        ('none', 'Без ссылки'),
    ]
    link_type = models.CharField('Тип ссылки', max_length=10,
                                 choices=LINK_TYPES, default='category')
    link_category = models.ForeignKey(Category, models.SET_NULL,
                                      null=True, blank=True,
                                      verbose_name='Категория',
                                      help_text='Если выбран тип "Категория"')
    link_product = models.ForeignKey(Product, models.SET_NULL,
                                     null=True, blank=True,
                                     verbose_name='Товар',
                                     help_text='Если выбран тип "Товар"')
    link_url = models.URLField('Произвольный URL', blank=True,
                               help_text='Если выбран тип "Произвольный URL"')

    products = models.ManyToManyField(Product,
                                      verbose_name='Товары акции',
                                      related_name='banners',
                                      blank=True,
                                      help_text='Товары, участвующие в этой акции')

    is_active = models.BooleanField('Активен', default=True)
    order = models.PositiveIntegerField('Порядок', default=0,
                                        help_text='Чем меньше число, тем выше баннер')

    start_date = models.DateTimeField('Дата начала', null=True, blank=True,
                                      help_text='Если не указано, баннер показывается всегда')
    end_date = models.DateTimeField('Дата окончания', null=True, blank=True,
                                    help_text='Если не указано, баннер показывается всегда')

    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)

    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннеры'
        ordering = ['order', '-created_at']
        indexes = [
            models.Index(fields=['is_active', '-order']),
        ]

    def __str__(self):
        return f"Баннер {self.title or self.id} ({'активен' if self.is_active else 'неактивен'})"

    def get_link(self):
        """Возвращает URL для перехода"""
        if self.link_type == 'category' and self.link_category:
            return self.link_category.get_absolute_url()
        elif self.link_type == 'product' and self.link_product:
            return self.link_product.get_absolute_url()
        elif self.link_type == 'custom' and self.link_url:
            return self.link_url
        return '#'

    def get_discounted_products(self, count=3):
        """Возвращает товары из акции (не только со скидкой)"""

        if self.products.exists():
            return self.products.all().order_by('?')[:count]
        return []

    @property
    def is_current(self):
        """Проверяет, актуален ли баннер по датам"""
        from django.utils import timezone
        now = timezone.now()
        if self.start_date and now < self.start_date:
            return False
        if self.end_date and now > self.end_date:
            return False
        return True