from categories.models import Category

from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=1000)
    category = models.ForeignKey(Category, models.PROTECT)
    creator = models.ForeignKey(User, models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Commit(models.Model):
    post = models.ForeignKey(Post, models.CASCADE)
    content = models.TextField(max_length=1000)
    creator = models.ForeignKey(User, models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
