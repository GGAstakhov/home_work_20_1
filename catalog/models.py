from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from src.constants import NULLABLE
from users.models import User


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    image = models.ImageField(upload_to='media/', **NULLABLE, verbose_name='Изображение')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена покупки')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    date_modified = models.DateTimeField(auto_now=True, verbose_name='Последняя измененная дата')

    # Поле для хранения пользователя, который создал продукт
    owner = models.ForeignKey(User, on_delete=models.PROTECT, **NULLABLE)
    is_published = models.BooleanField(default=False, verbose_name='признак публикации', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    description = models.TextField(**NULLABLE, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


# Описание модели Версий
class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    number = models.PositiveIntegerField(validators=[MinValueValidator(1)], verbose_name='Номер версии')
    name = models.CharField(max_length=150, verbose_name='Имя версии')
    is_active = models.BooleanField(default=False, verbose_name='Признак текущей версии')

    def __str__(self):
        return f'{self.product.name} - Версия: {self.number}'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'

