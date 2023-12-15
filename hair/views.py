from django.shortcuts import render


def index(request):
    return render(request, "hair/index.html")


def get_page(request, slug):
    return render(request, "hair/index.html")


def gallery(request):
    return render(request, "hair/gallery.html")
