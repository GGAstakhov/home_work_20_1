from django.contrib import admin

from catalog.models import Product, Category


# Product name in admin panel
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'description')
    verbose_name_plural = 'Продукты'


# Category name in admin panel
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    verbose_name_plural = 'Категории'
