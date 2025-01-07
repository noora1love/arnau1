# Generated by Django 5.1.4 on 2024-12-17 13:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_category_options_category_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='TableCloth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='oilcloth_images/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='oilcloths', to='main.category')),
            ],
            options={
                'verbose_name': 'Клеёнка',
                'verbose_name_plural': 'Клеёнки',
            },
        ),
    ]
