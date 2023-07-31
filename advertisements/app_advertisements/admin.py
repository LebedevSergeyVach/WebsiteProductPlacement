from django.contrib import admin
from .models import Advertisement


# Register your models here.

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'auctions', 'created_date', 'updated_at']
    list_filter = ['auctions', 'created_at', 'updated_at']
    actions =['make_auctions_as_false', 'make_auctions_as_true']
    fieldsets = (
        ('Общая информация', {
            'fields': ('title', 'description')
        }),

        ('Цены', {
            'fields': ('price', 'auctions'),
            'classes': ['collapse']
        })
    )

    @admin.action(description='Убрать возможность торга')
    def make_auctions_as_false(self, request, queryset):
        queryset.update(auctions=False)

    @admin.action(description='Добавить возможность торга')
    def make_auctions_as_true(self, request, queryset):
        queryset.update(auctions=True)


admin.site.register(Advertisement, AdvertisementAdmin)
