import csv

from django.contrib import admin
from django.http import HttpResponse

from .models import Places, PlaceImages
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableInlineAdminMixin



class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"

class InlinePlaceImages(SortableInlineAdminMixin,admin.TabularInline):
    model = PlaceImages
    list_display_links = None
    list_display = ['position']
    fields = ('position','image', 'get_preview_image', )
    readonly_fields = ['get_preview_image']
    extra = 1

    def get_preview_image(self, obj):
        return mark_safe('<img src="/media/{url}" width="{width}" height={height} />'.format(
            url=obj.image,
            width=400,
            height=200,
        )
        )


@admin.register(PlaceImages)
class PlaceImagesAmdin(admin.ModelAdmin,ExportCsvMixin):
    list_display = ['position']
    readonly_fields = ['get_preview_image']

    def get_preview_image(self, obj):
        return mark_safe('<img src="/media/{url}" width="{width}" height={height} />'.format(
            url=obj.image,
            width=400,
            height=200,
        )
        )


@admin.register(Places)
class PlacesAdmin(admin.ModelAdmin):
    inlines = [
        InlinePlaceImages,
    ]





