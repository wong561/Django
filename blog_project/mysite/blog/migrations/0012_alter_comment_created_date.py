# Generated by Django 3.2.15 on 2023-07-22 21:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_comment_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 22, 21, 28, 41, 829031, tzinfo=utc)),
        ),
    ]