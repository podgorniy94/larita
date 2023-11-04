from django.urls import path
from hair.views import index

urlpatterns = [
    path("test/", index),
]
