# Generated by Django 2.2.4 on 2019-08-23 18:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 23, 18, 33, 49, 300385), verbose_name='date published'),
        ),
    ]
