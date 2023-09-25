from django.core.management import BaseCommand
from catalog.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        category_list = [
            {'name': 'smartphones and gadgets', 'description': 'This section presents various smartphones and gadgets'},
            {'name': 'computer furniture', 'description': 'This section presents computer chairs and tables from famous brands'},
            {'name': 'computers and laptops', 'description': 'This section presents laptops, monitors and desktop computers'},
            {'name': 'TVs', 'description': 'This section presents TVs from large and well-known brands'},
        ]

        Category.objects.all().delete()

        categories_for_create = []
        for category_item in category_list:
            categories_for_create.append(
                Category(**category_item)
            )

        Category.objects.bulk_create(categories_for_create)
