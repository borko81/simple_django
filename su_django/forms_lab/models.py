from django.db import models


class Todo(models.Model):
    name = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=20)
    text = models.TextField()

    def __str__(self):
        return self.name
