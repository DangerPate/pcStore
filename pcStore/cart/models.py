# cart/models.py
from django.db import models
from django.conf import settings
from catalog.models import Product

class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cart')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return f"Корзина {self.user.email}"

    def get_total_price(self):
        # 🔑 Вызываем метод у каждого элемента
        return sum(item.get_total_price() for item in self.items.all())

    def get_total_quantity(self):
        return sum(item.quantity for item in self.items.all())


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_items')
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = 'Позиция корзины'
        unique_together = ('cart', 'product')
        indexes = [
            models.Index(fields=['cart', 'product']),  # 🔑 Ускоряет поиск
        ]

    def __str__(self):
        return f"{self.product.title} × {self.quantity}"

    # 🔑 ОБЯЗАТЕЛЬНЫЙ МЕТОД — без него падает ошибка
    def get_total_price(self):
        return self.product.price * self.quantity


class Favorite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='favorites')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='favorited_by')
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Избранное'
        unique_together = ('user', 'product')
        ordering = ['-added_at']
        indexes = [
            models.Index(fields=['user', 'product']),  # 🔑 Ускоряет проверку "в избранном"
        ]

    def __str__(self):
        return f"{self.product.title}"