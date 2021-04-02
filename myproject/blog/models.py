from django.db import models
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('articles:article-detail', kwargs={"pk": self.id})
