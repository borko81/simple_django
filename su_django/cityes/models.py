from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    town = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name