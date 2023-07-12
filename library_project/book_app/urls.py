from django.urls import path
from django.conf.urls import url
from . import views


app_name = 'book_app'


urlpatterns = [
    url(r'^update/(?P<pk>\d+)/$',views.AuthorUpdateView.as_view(),name='update'),
    # path('update/<int:pk>/', views.AuthorUpdateView.as_view(), name='update'),
    path('create/', views.AuthorCreateView.as_view(), name='create'),
    path('<int:pk>/', views.AuthorDetailView.as_view(), name='author_detail'),
    path('home', views.IndexView.as_view(), name="home"),
    path('author_list/', views.AuthorListView.as_view(), name='author_list'),
    path('delete/<int:pk>/', views.AuthorDeleteView.as_view(), name='delete'),
    path('update/<int:pk>/', views.BookUpdate.as_view(), name='book_update'),
    path('create/', views.BookCreateView.as_view(), name='book_create'),
    path('books/<int:pk>/', views.BookDetail.as_view(), name='book_detail'),
    path('books/books_index/', views.books_index_view, name='book_list'),
    path('book_delete/<int:pk>/', views.AuthorDeleteView.as_view(), name='book_delete'),
    # path('whatever/', views.AuthorListView.as_view(), name='author_list'),
]
