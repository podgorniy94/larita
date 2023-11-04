from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    slug = models.SlugField(max_length=255, verbose_name="URL", unique=True)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Опубликовано")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Статья(ю)"
        verbose_name_plural = "Статьи"
        ordering = ["-created_at"]


#    def get_absolute_url(self):
#        return reverse("post", kwargs={"slug": self.slug})
