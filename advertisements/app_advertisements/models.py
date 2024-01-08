from django.db import models
from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html
from django.contrib.auth import get_user_model
from django.urls import reverse


# Create your models here.


User = get_user_model()


class Advertisement(models.Model):
    """Advertisement model"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
    )

    image_1 = models.ImageField(
        verbose_name="Изображение",
        upload_to="advertisements/",
        null=True,
        blank=True,
    )

    image_2 = models.ImageField(
        verbose_name="Дополнительное Изображение",
        upload_to="advertisements/",
        null=True,
        blank=True,
    )

    image_3 = models.ImageField(
        verbose_name="Дополнительное Изображение",
        upload_to="advertisements/",
        null=True,
        blank=True,
    )

    title = models.CharField(
        verbose_name="Заголовок",
        max_length=100,
    )

    description = models.TextField(
        verbose_name="Описание",
        max_length=1000,
    )

    price = models.DecimalField(
        verbose_name="Цена",
        max_digits=10,
        decimal_places=2,
    )

    auction = models.BooleanField(
        verbose_name="Аукцион",
        default=False,
    )

    email = models.EmailField(
        verbose_name="Электронная почта",
        max_length=50,
        null=True,
        blank=True,
    )

    contact = models.CharField(
        verbose_name="Контакты",
        max_length=20,
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @admin.display(description="Дата создания")
    def created_date(self):
        """Show the date of the creation"""
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M:%S")

            return format_html(
                '<span style="color: blue; font-weight: bold;">Сегодня в {}</span>', created_time
            )

        return self.created_at.strftime("%d.%m.%Y в %H:%M:%S")

    @admin.display(description="Дата изменения")
    def updated_date(self):
        """Show the date of the update"""
        if self.updated_at.date() == timezone.now().date():
            created_time = self.updated_at.time().strftime("%H:%M:%S")

            return format_html(
                '<span style="color: green; font-weight: bold">Сегодня в {}</span>', created_time
            )

        return self.updated_at.strftime(f"%d.%m.%Y в %H:%M:%S")

    @admin.display(description="Аукцион")
    def show_auction(self):
        """Show the auction status"""
        if self.auction:
            return format_html(
                '<span style="color: blue; font-weight: bold;">🍏</span>'
            )
        else:
            return format_html(
                '<span style="color: red; font-weight: bold;">🍎</span>'
            )

    @admin.display(description="Изображения")
    def show_image_1(self):
        """Show the image"""
        if self.image_1:
            return format_html(
                '<img src={} style="width: 70px; height: 50px">', self.image_1.url
            )
        else:
            return format_html(
                '<img src="https://pa1.narvii.com/7435/efabf45acf29e0c694a56ec3871779f6f5434fc7r1-640-360_hq.gif"'
                'style="width: 70px; height: 50px">'
            )

    @admin.display(description="Изображения")
    def show_image_2(self):
        """Show the image"""
        if self.image_2:
            return format_html(
                '<img src={} style="width: 70px; height: 50px">', self.image_2.url
            )
        else:
            return format_html(
                '<img src="https://pa1.narvii.com/7435/efabf45acf29e0c694a56ec3871779f6f5434fc7r1-640-360_hq.gif"'
                'style="width: 70px; height: 50px">'
            )

    @admin.display(description="Изображения")
    def show_image_3(self):
        """Show the image"""
        if self.image_3:
            return format_html(
                '<img src={} style="width: 70px; height: 50px">', self.image_3.url
            )
        else:
            return format_html(
                '<img src="https://pa1.narvii.com/7435/efabf45acf29e0c694a56ec3871779f6f5434fc7r1-640-360_hq.gif"'
                'style="width: 70px; height: 50px">'
            )

    @admin.display(description="Почта")
    def show_email(self):
        """Show the contact information"""
        if self.user.is_superuser:
            return format_html(
                '<span style="color: red; font-weight: bold;">Администратор</span>'
            )
        else:
            return format_html(
                '<span style="color: blue; font-weight: bold;">{}</span>', self.user.email
            )

    @admin.display(description="Пользователь")
    def show_user(self):
        """Show the user"""
        if self.user.is_superuser:
            return format_html(
                '<span style="color: red; font-weight: bold;">Администратор</span>'
            )
        else:
            return format_html(
                '<span style="color: blue; font-weight: bold;">{}</span>', self.user.username
            )

    @admin.display(description="Контакты")
    def show_contact(self):
        """Show the contact"""
        if self.user.is_superuser:
            return format_html(
                '<span style="color: red; font-weight: bold;">Администратор</span>'
            )
        else:
            return format_html(
                '<span style="color: blue; font-weight: bold;">{}</span>', self.contact
            )

    def __str__(self):
        """String representation"""
        return f"id = {self.id} title = {self.title} price = {self.price}"

    def get_absolute_url(self):
        """Get absolute URL for this user from the database"""
        return reverse(
            "advertisement", kwargs={"pk": self.pk}
        )

    class Meta:
        """Meta options"""
        db_table = "advertisement"
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
