# Generated by Django 3.1.7 on 2021-03-24 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_valid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='valid',
            field=models.BooleanField(default=True),
        ),
    ]
