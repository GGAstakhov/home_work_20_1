# Generated by Django 4.2.5 on 2024-04-24 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_product_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_published',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='признак публикации'),
        ),
    ]
