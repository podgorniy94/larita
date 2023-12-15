from django.urls import path

from hair.views import gallery, get_page, index

app_name = "hair"

urlpatterns = [
    path("", index, name="home"),
    path("gallery", gallery, name="gallery"),
    path("<str:slug>", get_page, name="page"),
]
