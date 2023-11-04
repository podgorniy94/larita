from django.contrib import admin
from django.urls import include, path

# {% url 'hair:name' id %}, namespace="hair"
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("hair.urls")),
]
