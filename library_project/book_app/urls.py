from django.urls import path
from . import views

urlpatterns=[
    path('',views.homeview_function, name="home"),
]