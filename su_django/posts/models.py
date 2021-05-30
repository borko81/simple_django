from django.db import models


class Post(models.Model):
    post_heading = models.CharField(max_length=25)
    post_text = models.TextField()
    post_author = models.CharField(max_length=100, default='anonymous')

    def __str__(self):
        return self.post_heading


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.post.post_heading
