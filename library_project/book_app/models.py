from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("simon:author_detail", kwargs={"pk": self.id})


class Book(models.Model):
    title = models.CharField(max_length=255)
    year_published = models.IntegerField(null=True)
    author = models.ForeignKey(
        Author, related_name='book', on_delete=models.CASCADE)
    rating = models.FloatField(null=True)
    cover = models.TextField(blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("simon:book_detail", kwargs={"pk": self.id})
