from django.urls import path

from hair.views import index

app_name = "hair"

urlpatterns = [
    path("", index),
]
