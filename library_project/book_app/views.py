from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import (View, TemplateView,
                                  ListView, DetailView,
                                  CreateView, UpdateView,
                                  DeleteView)

from django.db import models
from django.urls import reverse_lazy
from . import models
# from book_app.models import Book
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
    template_name = 'authors/author_list.html'


class AuthorDetailView(DetailView):
    context_object_name = 'author_detail'
    model = models.Author
    template_name = 'authors/author_detail.html'


class AuthorCreateView(CreateView):
    fields = ('name', 'age')
    model = models.Author

    def form_valid(self, form):
        return super().form_valid(form)


class AuthorUpdateView(UpdateView):
    fields = ('name', 'age')
    model = models.Author


class AuthorDeleteView(DeleteView):
    model = models.Author
    success_url = reverse_lazy("simon:delete")


def books_index_view(request):
    books_from_db = models.Book.objects.all()
    return render(request, 'book_app/book_list.html', {'books': books_from_db})


class BookDetailView(DetailView):
    model = models.Book
    template_name = 'book_app/book_detail.html'
    context_object_name="book"

class BookCreateView(CreateView):
    model = models.Book
    fields = ['title', 'year_published', 'cover', 'author']
    template_name = 'book_app/book_form.html' 
    success_url = reverse_lazy('book_app:book_detail')
    
    def form_valid(self, form):
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('book_app:book_list') 

class BookUpdate(UpdateView):
    model = models.Book
    fields = '__all__'
    template_name = 'book_app/book_form.html'
    success_url = reverse_lazy('book_app:book_list')

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)
    
    
    

class BookDeleteView(DeleteView):
    model = models.Book
    success_url = reverse_lazy('book_app:book_list')
