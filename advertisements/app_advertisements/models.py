from enum import auto

from django.db import models
from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html


# Create your models here.


class Advertisement(models.Model):
    title = models.CharField(
        verbose_name="Заголовок",
        help_text="Сюда пишем заголовок товара",
        max_length=100,
    )

    description = models.TextField(
        verbose_name="Описание",
        help_text="Сюда пишем описание товара",
        max_length=1000,
    )

    price = models.DecimalField(
        verbose_name="Цена",
        help_text="Сюда пишем цену товара",
        max_digits=10,
        decimal_places=2,
    )

    auctions = models.BooleanField(
        verbose_name="Аукцион",
        help_text="Сюда пишем аукцион товара",
        default=False,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @admin.display(description="Дата создания")
    def created_date(self):
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M:%S")
            return format_html(
                '<span style="color: green; font-weight: bold;">Сегодня в {}</span>', created_time
            )
        return self.created_at.strftime("%d.%m.%Y в %H:%M:%S")

    def __str__(self):
        return f'id = {self.id} title = {self.title} description = {self.description} price = {self.price}'

    class Meta:
        db_table = "advertisement"
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
