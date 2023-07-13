from django.urls import path
from django.conf.urls import url
from . import views


app_name = 'book_app'

urlpatterns = [
    path('',views.IndexView.as_view(),name='home'),
    path('title/', views.BookCreateView.as_view(), name='book_create'),
    # path('authors/author_list/<int:pk>/', views.AuthorUpdateView.as_view(), name='update'),
    path('authors/author_list/', views.AuthorListView.as_view(), name='author_list'),
    # path('update/<int:pk>/', views.BookUpdate.as_view(), name='book_update'),
    path('<int:pk>/', views.books_index_view, name='book_detail'),
    path('create/', views.AuthorCreateView.as_view(), name='create'),
    path('authors/<int:author_id>/', views.AuthorDetailView.as_view(), name='author_detail'),
    path('books_index/', views.books_index_view, name='book_list'),
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
#     path('<int:pk>/', views.BookDetail.as_view(), name='book_detail'),
#     
#     path('book_delete/<int:pk>/', views.AuthorDeleteView.as_view(), name='book_delete'),
#     # path('whatever/', views.AuthorListView.as_view(), name='author_list'),
# ]
