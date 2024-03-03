from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from unidecode import unidecode

NULLABLE = {'blank': True, 'null': True}


# Создание модели Blog
class Blog(models.Model):
    name = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.CharField(max_length=100, verbose_name='Slug')
    content = models.TextField(**NULLABLE, verbose_name='Содержимое')
    preview = models.ImageField(upload_to='blog/media/blog/blog', **NULLABLE, verbose_name="Превью")
    date_create = models.DateTimeField(**NULLABLE, verbose_name='Дата создания')
    published = models.BooleanField(default=False, verbose_name="Опубликован")
    count_views = models.IntegerField(default=0, verbose_name='Количество просмотров')

    # Автоматическое формирование slug и date_create
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.name))
        if not self.pk:
            self.date_create = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'

    # Мета данные: отображаемые имена моделей
    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
