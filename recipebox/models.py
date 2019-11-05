"""
Author:
    Name
    Bio (`TextField`)

Recipe:
    Title
    Author (ForeignKey)
    Description
    Time Required
    Instructions (`TextField`)
"""
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name



class Recipe(models.Model):
    title = models.CharField(max_length=64)
    author = models.ForeignKey("Author", on_delete=models.CASCADE)
    description = models.CharField(max_length=64)
    time_required = models.IntegerField()
    instructions = models.TextField()

    def __str__(self):
        return f"{self.title} - by {self.author.name}"

