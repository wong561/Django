from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'shop'


urlpatterns = [
    path('',views.index, name='index'),
    path('<int:id/',views.detail,name='detail'),
]
