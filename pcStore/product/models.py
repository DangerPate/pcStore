from django.db import models

class Product(models.Model):
    title = models.CharField('Название', max_length=50)
    info = models.TextField('Информация о товаре', blank=True)
    price = models.IntegerField('Цена')
    image = models.ImageField(
        upload_to='products/%Y/%m/%d/',
        blank=True,
        null=True,
        verbose_name='Изображение товара'
    )
    in_stock = models.IntegerField('В наличии')
    warranty = models.IntegerField('Гарантия')
    categories = models.ManyToManyField('Category', blank=True, related_name='products')
    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField('Название', max_length=50)

    def __str__(self):
        return self.title