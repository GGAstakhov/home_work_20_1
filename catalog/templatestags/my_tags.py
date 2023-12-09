from django import template

register = template.Library()

# Создание Кастомного тега, который используется в шаблоне и указывает полный путь к медиа-файлам
@register.filter()
def mymedia(value):
    if value:
        return f'/catalog/media/catalog/{value}/'

    return f'/catalog/media/catalog/img.png/'
