from django.contrib import admin

from .models import GalleryPhoto, Page, Tag


class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class GalleryPhotoAdmin(admin.ModelAdmin):
    save_as = True


admin.site.register(Page, PageAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(GalleryPhoto, GalleryPhotoAdmin)
