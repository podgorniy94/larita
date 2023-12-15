from django.urls import path

from hair.views import Gallery, Home, Page

app_name = "hair"

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("gallery", Gallery.as_view(), name="gallery"),
    path("<slug:slug>", Page.as_view(), name="page"),
]
