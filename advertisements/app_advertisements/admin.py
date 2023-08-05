from django.contrib import admin
from .models import Advertisement


class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'created_date', 'auction']
    list_filter = ['auction', 'created_at']
    actions = ['make_auction_as_false', 'make_auction_as_true']
    fieldsets = (
        ('General', {
            'fields': ('title', 'description')
            }
         ),
        ('Finances', {
            'fields': ('price', 'auction'),
            'classes': ['collapse']
            }
         )
    )

    @admin.action(description='Remove the possibility of sale')
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction=False)

    @admin.action(description='Add the possibility of sale')
    def make_auction_ad_true(self, request, queryset):
        queryset.update(auction=True)


admin.site.register(Advertisement, AdvertisementAdmin)
