from django.contrib import admin
from book_app.models import Author, BookTitle

# Register your models here.
admin.site.register(Author)
admin.site.register(BookTitle)