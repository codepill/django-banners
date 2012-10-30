from django.contrib import admin
from django.contrib.admin.views.main import ChangeList
from models import *


class BannerAdmin(admin.ModelAdmin):
    list_display = ('order_link', 'id', 'slot', 'title', 'is_published', 'popup', 'destination_url',)
    list_display_links = ('id', 'title',)
    list_filter = ('is_published', 'slot', 'popup',)
    search_fields = ('id', 'title', )
    exclude = ('display_order',)
    ordering = ('display_order', 'id',)
    fieldsets = (
        (None, {'fields': (
            'title', 'slot', 'is_published', 'popup', 'banner_file',
            'image_rollover', 'destination_url',
            )}),
        )

    class Media:
        js = ("js/libs/jquery-1.6.2.min.js",
              "js/jquery-ui-1.8.16.custom.min.js",
              "js/admin_sorting.js",
              "js/admin_update_imagefield_list.js",)
        css = {
            "all": ("css/admin_sortablelist.css",
                    "css/admin_inline_list.css",),
        }

    class CustomOrderingChangeList(ChangeList):
        def get_ordering(self, request, queryset):
            return ['display_order']

        def get_ordering_field_columns(self):
            return {}

    def get_ordering(self, request):
        return ['display_order']

    def get_changelist(self, request, **kwargs):
        return self.CustomOrderingChangeList

    def order_link(self, instance):
        model_type_id = ContentType.objects.get_for_model(instance.__class__).pk
        url = reverse("admin_order", kwargs={'model_type_id': model_type_id})
        return '<a href="%s" class="order_link">%s</a>' % (url, str(instance.pk) or '')

    order_link.allow_tags = True


class SlotAdmin(admin.ModelAdmin):
    list_display = ('name', 'symbol', 'language')
    list_filter = ('language',)


admin.site.register(Banner, BannerAdmin)
admin.site.register(Slot, SlotAdmin)
