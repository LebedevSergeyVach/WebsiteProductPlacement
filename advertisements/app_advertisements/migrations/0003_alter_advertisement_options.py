# Generated by Django 4.2.4 on 2023-08-17 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisements', '0002_alter_advertisement_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='advertisement',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
    ]
