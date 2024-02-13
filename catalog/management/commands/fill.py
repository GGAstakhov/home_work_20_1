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
        # cleaning old files
        Category.objects.all().delete()

        # Creating and saving new category objects
        categories_for_create = [Category(**category) for category in category_list]
        Category.objects.bulk_create(categories_for_create)

        self.stdout.write(self.style.SUCCESS('Данные успешно добавлены.'))
