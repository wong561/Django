# Generated by Django 3.2.15 on 2023-07-12 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0007_book_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.TextField(blank=True),
        ),
    ]
