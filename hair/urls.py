from django.urls import path
from hair.views import About, Contact, Gallery, Home, Page, Services

app_name = "hair"

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("about", About.as_view(), name="about"),
    path("services", Services.as_view(), name="services"),
    path("gallery", Gallery.as_view(), name="gallery"),
    path("contact", Contact.as_view(), name="contact"),
    path("<slug:slug>", Page.as_view(), name="page"),
]
