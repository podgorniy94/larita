from django.contrib import admin

from .models import GalleryPhoto, Page, Tag

admin.site.register(Page)
admin.site.register(Tag)
admin.site.register(GalleryPhoto)
