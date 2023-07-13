from django.shortcuts import render
from django.views.generic import (View, TemplateView,
                                  ListView, DetailView,
                                  CreateView, UpdateView,
                                  DeleteView)

from django.db import models
from django.urls import reverse_lazy
from . import models
from book_app.models import Book
from django.contrib.auth.decorators import login_required
# Create your views here.
# def index(request):
# return (render(request,'index.html'))


class IndexView(TemplateView):
    context_object_name = 'home'
    template_name = 'index.html'


class AuthorListView(ListView):
    context_object_name = 'authors'
    model = models.Author
    template_name = 'book_app/author_list.html'


class AuthorDetailView(DetailView):
    context_object_name = 'author_detail'
    model = models.Author
    template_name = 'book_app/authors/author_detail.html'


class AuthorCreateView(CreateView):
    fields = ('name', 'age')
    model = models.Author


class AuthorUpdateView(UpdateView):
    fields = ('name', 'age')
    model = models.Author


class AuthorDeleteView(DeleteView):
    model = models.Author
    success_url = reverse_lazy("book_app:list")


def books_index_view(request):
    books_from_db = Book.objects.filter()
    return render(request,'books/books_index.html',{'books_for_template':books_from_db})

class BookDetail(DetailView):
    model=Book 
    template_name = 'books/book_detail.html'

class BookCreateView(CreateView):
    model=Book
    fields=['title','year_published','cover','author']

    def form_valid(self,form):
        return super().form_valid(form)
    

class BookUpdate(UpdateView):
    model=Book
    fields='__all__'
    # success_url = reverse_lazy("book_app:list")

class BookDeleteView(DeleteView):
    model=Book
    success_url='/books/'
