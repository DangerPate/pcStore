# cart/models.py
from django.db import models
from django.conf import settings
from catalog.models import Product

class CartItem(models.Model):
    """Позиция корзины — привязана напрямую к пользователю"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='cart_items'
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Позиция корзины'
        verbose_name_plural = 'Позиции корзины'
        unique_together = ('user', 'product')  # Один товар у пользователя — одна запись
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['user', 'product']),
        ]

    def __str__(self):
        return f"{self.product.title} × {self.quantity} (user: {self.user.email})"

    def get_total_price(self):
        """Стоимость этой позиции (цена × количество)"""
        return self.product.price * self.quantity


class Favorite(models.Model):
    """Избранное — привязано напрямую к пользователю"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='favorites'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='favorited_by'
    )
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'
        unique_together = ('user', 'product')
        ordering = ['-added_at']
        indexes = [
            models.Index(fields=['user', 'product']),
        ]

    def __str__(self):
        return f"{self.product.title} in favorites of {self.user.email}"


# 🔹 Заглушка для модели Cart (если где-то в коде остались ссылки)
# Можно удалить, если нигде не используется
class Cart(models.Model):
    """
    ЗАГЛУШКА — не используется.
    Корзина теперь работает напрямую через CartItem → User.
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='cart',
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Корзина (заглушка)'
        verbose_name_plural = 'Корзины (заглушка)'

    def __str__(self):
        return f"Cart of {self.user.email if self.user else 'Anonymous'}"


class Order(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новый'),
        ('processing', 'В обработке'),
        ('completed', 'Выполнен'),
        ('cancelled', 'Отменен'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True,
                             verbose_name='Пользователь')
    first_name = models.CharField('Имя', max_length=100)
    phone = models.CharField('Телефон', max_length=20)
    email = models.EmailField('Email', blank=True, null=True)
    address = models.TextField('Адрес доставки')
    comment = models.TextField('Комментарий к заказу', blank=True)
    total_price = models.DecimalField('Общая сумма', max_digits=10, decimal_places=2)
    status = models.CharField('Статус', max_length=20, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-created_at']

    def __str__(self):
        return f"Заказ #{self.id} от {self.first_name}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', verbose_name='Заказ')
    # Используем строку 'catalog.Product', чтобы избежать циклического импорта
    product = models.ForeignKey('catalog.Product', on_delete=models.PROTECT, verbose_name='Товар')
    price = models.DecimalField('Цена на момент заказа', max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField('Количество', default=1)

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'

    def get_total_price(self):
        return self.price * self.quantity

    def __str__(self):
        return f"{self.product.title} x {self.quantity}"