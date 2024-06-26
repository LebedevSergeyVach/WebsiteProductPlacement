from django.contrib import admin
from .models import Advertisement


# Register your models here.

class AdvertisementAdmin(admin.ModelAdmin):
    """Advertisement Admin"""
    list_display = [
        'id', 'show_user', 'show_contact', 'show_email', 'title',
        'description', 'price', 'created_date', 'updated_date',
        'show_auction', 'show_image_1', 'show_image_2', 'show_image_3',
    ]

    list_filter = [
        'auction', 'created_at', 'updated_at'
    ]

    actions = [
        'make_auction_as_false', 'make_auction_as_true'
    ]

    fieldsets = (
        ('Общая информация', {
            'fields': ('title', 'description', 'user', 'image_1', 'image_2', 'image_3')
        }),

        ('Цены', {
            'fields': ('price', 'auction'),
            'classes': ['collapse']
        })
    )

    @admin.action(description="Убрать возможность торга")
    def make_auction_as_false(self, request, queryset):
        """Remove the possibility of bargaining"""
        queryset.update(auction=False)

    @admin.action(description="Добавить возможность торга")
    def make_auction_as_true(self, request, queryset):
        """Make the possibility of bargaining"""
        queryset.update(auction=True)


admin.site.register(Advertisement, AdvertisementAdmin)
