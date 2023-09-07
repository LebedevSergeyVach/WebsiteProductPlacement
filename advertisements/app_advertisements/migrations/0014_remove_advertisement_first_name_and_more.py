# Generated by Django 4.2.5 on 2023-09-07 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisements', '0013_advertisement_first_name_advertisement_last_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertisement',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='advertisement',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='advertisement',
            name='username',
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='contact',
            field=models.CharField(blank=True, max_length=2, null=True, verbose_name='Контакты'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='email',
            field=models.EmailField(blank=True, max_length=2, null=True, verbose_name='Электронная почта'),
        ),
    ]
