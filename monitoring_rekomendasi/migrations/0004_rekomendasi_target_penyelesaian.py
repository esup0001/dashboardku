# Generated by Django 3.2.7 on 2021-10-04 04:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring_rekomendasi', '0003_auto_20211004_0440'),
    ]

    operations = [
        migrations.AddField(
            model_name='rekomendasi',
            name='target_penyelesaian',
            field=models.DateField(default=datetime.datetime(2021, 10, 11, 4, 45, 32, 968356, tzinfo=utc)),
        ),
    ]