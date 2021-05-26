from django.db import models


class FileModels(models.Model):
    name = models.CharField(max_length=35)
    name_path = models.CharField(max_length=150)
    size = models.PositiveIntegerField()
    time_access = models.DateTimeField()
    modified = models.BooleanField(default=False)

    def __str__(self):
        return self.name
