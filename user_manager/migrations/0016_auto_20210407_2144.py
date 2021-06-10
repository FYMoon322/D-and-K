# Generated by Django 3.1.7 on 2021-04-07 16:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_manager', '0015_auto_20210407_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likes',
            name='unique_parameter',
            field=models.CharField(blank=True, max_length=50, unique=True, verbose_name='Уникальные параметр'),
        ),
        migrations.AlterField(
            model_name='news',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 7, 21, 44, 47, 690842), verbose_name='дата создания'),
        ),
        migrations.AlterField(
            model_name='repost',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 7, 21, 44, 47, 690842), verbose_name='дата создания'),
        ),
    ]