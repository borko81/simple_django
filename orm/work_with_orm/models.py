from django.contrib.auth.models import User
from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=20)
    data = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    add_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'cat'

    def __str__(self):
        return self.name


class UserParent(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CharField
    )
    father = models.CharField(max_length=20)
