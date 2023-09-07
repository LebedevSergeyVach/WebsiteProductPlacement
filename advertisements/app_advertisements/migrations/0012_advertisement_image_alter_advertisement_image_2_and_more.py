# Generated by Django 4.2.5 on 2023-09-07 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisements', '0011_remove_advertisement_favourites'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='advertisements/', verbose_name='Аватарка'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='image_2',
            field=models.ImageField(blank=True, null=True, upload_to='advertisements/', verbose_name='Дополнительное изображение'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='image_3',
            field=models.ImageField(blank=True, null=True, upload_to='advertisements/', verbose_name='Дополнительное изображение'),
        ),
    ]
