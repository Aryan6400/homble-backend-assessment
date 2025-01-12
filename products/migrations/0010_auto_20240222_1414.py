# Generated by Django 3.2.24 on 2024-02-22 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_add_price_in_sku'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sku',
            options={'ordering': [], 'verbose_name': 'Store Keeping Unit', 'verbose_name_plural': 'Store Keeping Units'},
        ),
        migrations.AlterField(
            model_name='sku',
            name='size',
            field=models.PositiveSmallIntegerField(blank=True, verbose_name='Size for the product(grams)'),
        ),
    ]
