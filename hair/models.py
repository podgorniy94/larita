from django.db import models
from django.urls import reverse


class Page(models.Model):
    title = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64, verbose_name="URL", unique=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("hair:page", kwargs={"slug": self.slug})

    class Meta:
        ordering = ["order"]
        verbose_name_plural = "Pages"


class Tag(models.Model):
    title = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64, verbose_name="URL", unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]
        verbose_name = "Tag"
        verbose_name_plural = "Tags"


class GalleryPhoto(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d")
    tags = models.ManyToManyField(Tag, blank=True, related_name="photos")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Photo"
        verbose_name_plural = "Photos"
