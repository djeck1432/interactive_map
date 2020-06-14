from django.contrib import admin
from .models import Place, PlaceImage
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableInlineAdminMixin

class InlinePlaceImages(SortableInlineAdminMixin,admin.TabularInline):
    model = PlaceImage
    list_display_links = None
    list_display = ['position']
    fields = ('position','image', 'get_preview_image', )
    readonly_fields = ['get_preview_image']
    extra = 1

    def get_preview_image(self, obj):
        return mark_safe('<img src="{url}" height="{height}" />'.format(
            url=obj.image.url,
            height=200,
        )
        )


@admin.register(PlaceImage)
class PlaceImagesAmdin(admin.ModelAdmin):
    list_display = ['place','position']
    readonly_fields = ['get_preview_image']
    list_filter = ['place']

    def get_preview_image(self, obj):
        return mark_safe('<img src="{url}" height="{height}" />'.format(
            url=obj.image.url,
            height=200,
        )
        )


@admin.register(Place)
class PlacesAdmin(admin.ModelAdmin):
    inlines = [
        InlinePlaceImages,
    ]






