from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
import random
import string

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
    email = models.EmailField('Email адрес', unique=True)
    phone = models.CharField('Телефон', max_length=15, unique=True)
    avatar = models.ImageField('Аватар', upload_to='users/avatars/', blank=True, null=True)
    nickname = models.CharField('Никнейм', max_length=50, blank=True)

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        db_table = 'users_user'

    def clean_nickname(self):
        import re
        if self.nickname and not re.match(r'^[\w\s\-\.]{3,50}$', self.nickname):
            raise ValidationError('Никнейм может содержать только буквы, цифры, пробелы, дефис и точку')
        return self.nickname

    def __str__(self):
        return self.get_display_name()

    def get_display_name(self):
        """Возвращает никнейм или авто-сгенерированный"""
        if self.nickname:
            return self.nickname

        return f"Пользователь-{self.id:07d}"

    def save(self, *args, **kwargs):

        if not self.nickname and self.pk is None:

            random_suffix = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
            self.nickname = f"Пользователь-{random_suffix}"
        super().save(*args, **kwargs)

class Review(models.Model):
    """Отзывы к товарам"""
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reviews')
    product = models.ForeignKey('catalog.Product', on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveSmallIntegerField('Рейтинг', default=5)
    comment = models.TextField('Комментарий', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Отзыв'
        unique_together = ('user', 'product')
