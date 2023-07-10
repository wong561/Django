from django.shortcuts import render
from django.views.generic import (View, TemplateView,
                                  ListView, DetailView,
                                  CreateView, UpdateView,
                                  DeleteView)
from . import models
from django.db import models
# Create your views here.
# def index(request):
    # return (render(request,'index.html'))

class CreateView(ListView):
    name=models.CharField(max_length=200)
    title=models.CharField(max_length=100)

class IndexView(TemplateView):
    context_object_name = 'home'
    template_name = 'index.html'
