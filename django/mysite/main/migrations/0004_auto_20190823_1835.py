# Generated by Django 2.2.4 on 2019-08-23 18:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20190823_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 23, 18, 35, 53, 491458, tzinfo=utc), verbose_name='date published'),
        ),
    ]
