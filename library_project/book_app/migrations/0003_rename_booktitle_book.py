# Generated by Django 3.2.15 on 2023-07-11 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0002_auto_20230711_0016'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BookTitle',
            new_name='Book',
        ),
    ]
