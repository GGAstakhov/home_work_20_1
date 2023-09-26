from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    description = models.TextField(**NULLABLE, verbose_name='Description')
    image = models.ImageField(upload_to='catalog/', **NULLABLE, verbose_name='Image')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Category')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Purchase price')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date of creation')
    date_modified = models.DateTimeField(auto_now=True, verbose_name='Last modified date')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    description = models.TextField(**NULLABLE, verbose_name='Description')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
