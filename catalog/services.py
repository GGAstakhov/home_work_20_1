from django.core.cache import cache
from catalog.models import Category
from config import settings


def get_cache_object_list():
    key = 'object_list'
    if settings.CACHE_ENABLED:
        object_list = cache.get(key)
        if object_list is None:
            object_list = Category.objects.all()
            cache.set(key, object_list)
    else:
        object_list = Category.objects.all()

    return object_list
