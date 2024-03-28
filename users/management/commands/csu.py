from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            first_name='admin',
            email='admin@sky.pro',
            last_name='SkyPro',
            is_superuser=True,
            is_staff=True,
        )

        user.set_password('admin')
        user.save()