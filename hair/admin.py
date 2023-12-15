from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import GalleryPhoto, Page, Tag


class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class GalleryPhotoAdmin(admin.ModelAdmin):
    save_as = True
    save_on_top = True
    list_display = ("id", "title", "created_at", "get_photo")
    list_display_links = ("id", "title")
    readonly_fields = ("created_at", "get_photo")

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        return "-"

    get_photo.short_description = "photo"


admin.site.register(Page, PageAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(GalleryPhoto, GalleryPhotoAdmin)
