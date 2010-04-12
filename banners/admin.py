from django.contrib import admin
from models import *

class BannerInline(admin.TabularInline):
    model = Banner

class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'slot', 'title', 'is_published', 'popup', 'display_order', 'destination', )
    list_display_links = ('id', 'title',)
    list_filter = ('is_published', 'slot','popup',)
    list_editable = ('display_order',)
    search_fields = ('id', 'title', )
    fieldsets = (
            (None,   {'fields': ('title', ('slot', 'is_published', 'popup',), 'image', 'image_rollover', 'destination', )}),
            )


class SlotAdmin(admin.ModelAdmin):
    inlines = [BannerInline]
    list_display = ('name', 'get_absolute_url')

admin.site.register(Banner, BannerAdmin)
admin.site.register(Slot, SlotAdmin)
