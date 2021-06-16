from django.db import models



class BookUserModel(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class BookModel(models.Model):
    title = models.CharField(max_length=20)
    pages = models.PositiveIntegerField(default=0)
    description = models.CharField(max_length=100)
    author = models.ForeignKey(BookUserModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
