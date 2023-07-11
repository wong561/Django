from django.shortcuts import render
from django.views.generic import (View, TemplateView,
                                  ListView, DetailView,
                                  CreateView, UpdateView,
                                  DeleteView)

from django.db import models
from django.urls import reverse_lazy
from . import models

# Create your views here.
# def index(request):
# return (render(request,'index.html'))

 
class IndexView(TemplateView):
    context_object_name = 'home'
    template_name = 'index.html'


class AuthorlListView(ListView):
    context_object_name = 'authors'
    model = models.Author


class AuthorDetailView(DetailView):
    context_object_name = 'author_detail'
    model = models.Author
    template_name = 'book_app/author_detail.html'


class AuthorCreateView(CreateView):
    fields = ('name',)
    model = models.Author


class AuthorUpdateView(UpdateView):
    fields = ('name',)
    model = models.Author


class AuthorDeleteView(DeleteView):
    model = models.Author
    success_url = reverse_lazy("book_app:list")
