from django.db import models
from django.urls import reverse



# Create your models here.
class Author(models.Model):
    
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("authors_detail", kwargs={"pk": self.id})
    