# Generated by Django 3.2.15 on 2023-07-03 03:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20230702_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 3, 3, 36, 40, 567655, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 3, 3, 36, 40, 566662, tzinfo=utc)),
        ),
    ]
