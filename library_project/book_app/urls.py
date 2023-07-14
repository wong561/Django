from django.urls import path
from django.conf.urls import url
from . import views


app_name = 'book_app'

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
     path('authors/create/', views.AuthorCreateView.as_view(), name='create'),
    path('books/create/', views.BookCreateView.as_view(), name='book_create'),
    path('authors/author_list/<int:pk>/',
         views.AuthorUpdateView.as_view(), name='update'),
    path('books/update/<int:pk>/', views.BookUpdate.as_view(), name='book_update'),
    path('author_list/', views.AuthorListView.as_view(), name='author_list'),
    path('books_list/', views.books_index_view, name='book_list'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('authors/<int:pk>/',
         views.AuthorDetailView.as_view(), name='author_detail'),    
    path('authors/delete/<int:pk>/', views.AuthorDeleteView.as_view(), name='delete'),
    path('books/delete/<int:pk>/', views.BookDeleteView.as_view(), name='book_delete'),
    
    # path('<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
]

# urlpatterns = [
#     url(r'^update/(?P<pk>\d+)/$',views.AuthorUpdateView.as_view(),name='update'),
#     #
#
#
#     path('home', views.IndexView.as_view(), name="home"),
#
#     path('delete/<int:pk>/', views.AuthorDeleteView.as_view(), name='delete'),
#
#     path('create/', views.BookCreateView.as_view(), name='book_create'),
#     
#
#     path('book_delete/<int:pk>/', views.AuthorDeleteView.as_view(), name='book_delete'),
#     # path('whatever/', views.AuthorListView.as_view(), name='author_list'),
# ]
