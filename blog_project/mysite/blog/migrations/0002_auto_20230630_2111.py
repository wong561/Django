# Generated by Django 3.2.15 on 2023-07-01 01:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 1, 1, 11, 6, 136317, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 1, 1, 11, 6, 135323, tzinfo=utc)),
        ),
    ]
