from enum import auto

from django.db import models

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

    def __str__(self):
        return f'ig = {self.id} title = {self.title} description = {self.description} price = {self.price}'

    class Meta:
        db_table = "advertisement"
