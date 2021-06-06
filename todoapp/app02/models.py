from django.db import models


class User(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    name = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
