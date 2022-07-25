from django.db import models
from django.conf import settings


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts",
        blank=True, null=True
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(
        auto_now_add=True, db_index=True
    )

    def __str__(self):
        return f"Post: {self.title}"


class Tag(models.Model):
    title = models.CharField(max_length=100)
    posts = models.ManyToManyField(Post)

    def __str__(self):
        return f"Tag: {self.title} with {self.posts.count()} post(s)"


class Adress(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts",
        blank=True, null=True
    )
    city = models.CharField(max_length=30)
    adress = models.CharField(max_length=60)


# Create your models here.
