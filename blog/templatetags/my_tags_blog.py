from django import template

register = template.Library()


# Создание Кастомного тега, который используется в шаблоне и указывает полный путь к медиа-файлам
@register.filter()
def mymedia_blog(value):
    if value:
        return f'/{value}/'

    return f'#'
