import csv

from django.contrib import admin
from django.http import HttpResponse

from .models import Place, PlaceImage
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableInlineAdminMixin

#
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
    model = PlaceImage
    list_display_links = None
    list_display = ['position']
    fields = ('position','image', 'get_preview_image', )
    readonly_fields = ['get_preview_image']
    extra = admin.TabularInline.extra

    def get_preview_image(self, obj):
        return mark_safe('<img src="/media/{url}" height={height} />'.format(
            url=obj.image,
            height=200,
        )
        )


@admin.register(PlaceImage)
class PlaceImagesAmdin(admin.ModelAdmin,ExportCsvMixin):
    list_display = ['place','position']
    readonly_fields = ['get_preview_image']
    list_filter = ['place']
    extra = 1

    def get_preview_image(self, obj):
        return mark_safe('<img src="/media/{url}" height={height} />'.format(
            url=obj.image,
            height=200,
        )
        )



@admin.register(Place)
class PlacesAdmin(admin.ModelAdmin):
    inlines = [
        InlinePlaceImages,
    ]





