# Generated by Django 3.2.24 on 2024-02-21 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_edited_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='ingredients',
            field=models.CharField(default='', help_text='Few sentences that provide the ingredients detail', max_length=500, verbose_name='ingredients detail'),
        ),
    ]
