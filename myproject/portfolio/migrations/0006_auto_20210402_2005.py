# Generated by Django 3.1.7 on 2021-04-02 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_auto_20210402_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FilePathField(blank=True, null=True, path='/img'),
        ),
    ]
