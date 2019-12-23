from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.name
