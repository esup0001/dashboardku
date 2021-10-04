# Generated by Django 3.2.7 on 2021-10-04 08:04

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring_rekomendasi', '0004_rekomendasi_target_penyelesaian'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rekomendasi',
            name='descripsi',
        ),
        migrations.AddField(
            model_name='pelatihan',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rekomendasi',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 10, 4, 8, 4, 21, 4781, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rekomendasi',
            name='deskripsi',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='rekomendasi',
            name='target_penyelesaian',
            field=models.DateField(default=datetime.datetime(2021, 10, 11, 8, 3, 47, 871769, tzinfo=utc)),
        ),
    ]
