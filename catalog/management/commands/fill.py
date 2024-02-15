from django.core.management import BaseCommand
from catalog.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        category_list = [
            {'name': 'Смартфоны, гаджеты', 'description': 'В этом разделе представлены различные смартфоны и гаджеты'},
            {'name': 'Компьютерная мебель', 'description': 'В этом разделе представлены компьютерные кресла и столы известных брендов'},
            {'name': 'Компьютеры, ноутбуки', 'description': 'В этом разделе представлены ноутбуки, мониторы и стационарные компьютеры'},
            {'name': 'Телевизоры', 'description': 'В этом разделе представлены телевизоры крупных и известных брендов'},
        ]

        Category.objects.all().delete()

        categories_for_create = []
        for category_item in category_list:
            categories_for_create.append(
                Category(**category_item)
            )

        Category.objects.bulk_create(categories_for_create)
