from django.urls import path
from . import views


app_name = 'book_app'


urlpatterns = [
    path('', views.IndexView.as_view(), name="list"),
    path('update/<int:pk>/', views.AuthorUpdateView.as_view(), name='update'),
    path('create/', views.AuthorCreateView.as_view(), name='create'),
]
    

