from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Поле Email обязательно для заполнения')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    # 🔑 Email обязателен и уникален
    email = models.EmailField('Email адрес', unique=True, blank=False)
    # 🔑 Телефон обязателен и уникален
    phone = models.CharField('Телефон', max_length=15, unique=True, blank=False)
    avatar = models.ImageField('Аватар', upload_to='users/avatars/', blank=True, null=True)

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        db_table = 'users_user'

    def __str__(self):
        return self.email


# === ЗАГОТОВКИ ПОД БУДУЩИЕ ФУНКЦИИ ===

class Review(models.Model):
    """Отзывы к товарам"""
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reviews')
    product = models.ForeignKey('catalog.Product', on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveSmallIntegerField('Рейтинг', default=5)
    comment = models.TextField('Комментарий', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Отзыв'
        unique_together = ('user', 'product')  # 1 отзыв от 1 пользователя на 1 товар


class Favorite(models.Model):
    """Избранное (явная модель для расширения: даты, заметки и т.д.)"""
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='favorites')
    product = models.ForeignKey('catalog.Product', on_delete=models.CASCADE, related_name='favorited_by')
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Избранное'
        unique_together = ('user', 'product')


class Cart(models.Model):
    """Корзина пользователя"""
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='cart')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CartItem(models.Model):
    """Товар в корзине"""
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('catalog.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('cart', 'product')