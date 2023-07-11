from django.db import models
from django.urls import reverse
from django.views.generic import TemplateView


# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=50)
    
    

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("book_app:detail", kwargs={"pk": self.pk})
    


class BookTitle(models.Model):
    title = models.CharField(max_length=256)
    rating = models.FloatField()
    author = models.ForeignKey(
        Author, related_name='titles', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
