# Generated by Django 2.1.7 on 2022-11-16 03:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20221116_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 11, 16, 0, 32, 55, 777123)),
        ),
    ]
