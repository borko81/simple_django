from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=50)
    technology = models.CharField(max_length=100)
    image = models.FilePathField(path='img/', null=True, blank=True)
