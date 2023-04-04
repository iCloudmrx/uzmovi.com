from django.db import models

# Create your models here.


class Film(models.Model):
    title = models.CharField(max_length=255, blank=False)
    slug = models.SlugField(max_length=255, blank=False, unique=True)
    imageUrl = models.CharField(blank=False, max_length=255)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
