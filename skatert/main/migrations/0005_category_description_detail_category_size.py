# Generated by Django 5.1.4 on 2025-01-15 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_image_tablecloth_image1_tablecloth_image2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description_detail',
            field=models.TextField(blank=True, null=True, verbose_name='Описание Детально'),
        ),
        migrations.AddField(
            model_name='category',
            name='size',
            field=models.TextField(blank=True, null=True, verbose_name='Размер (N x N)'),
        ),
    ]
