from django.contrib import admin
from .models import Advertisement


# Register your models here.

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'user', 'title', 'description', 'price', 'created_date', 'updated_date', 'show_auction', 'show_image'
    ]

    list_filter = [
        'auction', 'created_at', 'updated_at'
    ]

    auction = [
        'make_auction_as_false', 'make_auctios_as_true'
    ]

    fieldsets = (
        ('Общая информация', {
            'fields': ('title', 'description', 'user', 'image'),
        }),

        ('Цены', {
            'fields': ('price', 'auction'),
            'classes': ['collapse']
        })
    )

    @admin.action(description='Убрать возможность торга')
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction=False)

    @admin.action(description='Добавить возможность торга')
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)


admin.site.register(Advertisement, AdvertisementAdmin)
