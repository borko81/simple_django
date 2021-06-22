from django.db import models


class Pet(models.Model):
    CAT = 'cat'
    DOG = 'dog'
    PARROT = 'parrot'
    CHOICES = (
        ('CAT', CAT),
        ('DOG', DOG),
        ('PARROT', PARROT)
    )
    type = models.CharField(
        max_length=6,
        choices=CHOICES,
        default="CAT"
    )
    name = models.CharField(
        max_length=6
    )
    age = models.PositiveIntegerField()
    description = models.TextField()
    image_url = models.URLField()

    def __str__(self):
        return self.name


class Like(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)


class Comment(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    comment = models.TextField()

