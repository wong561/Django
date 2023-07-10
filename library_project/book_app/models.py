from django.db import models
from django.urls import reverse
from django.views.generic import TemplateView


# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=50)
    age=models.CharField(max_length=3)
    
    def __str__(self):
        return self.name, self.age
    
    def get_absolute_url(self):
        return reverse("authors_detail", kwargs={"pk": self.id})

class HomePage(TemplateView):
    template_name = "index.html"
