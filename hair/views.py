from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from .models import GalleryPhoto, Page


class Home(TemplateView):
    template_name = "hair/index.html"


class Page(ListView):
    model = Page
    template_name = "hair/index.html"
    context_object_name = "pages"


class Gallery(ListView):
    model = GalleryPhoto
    template_name = "hair/gallery.html"
    context_object_name = "photos"
    # allow_empty = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"], context["space"] = "Gallery", " "
        return context
