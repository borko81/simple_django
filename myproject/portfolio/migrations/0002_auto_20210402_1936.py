# Generated by Django 3.1.7 on 2021-04-02 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='iamge',
        ),
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.FilePathField(null=True, path='portfolio/img'),
        ),
    ]
