from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieSerializer
from .models import Moviedata


# Create your views here.
class MovieViewSet(viewsets.ModelViewSet):
    queryset=Moviedata.objects.all()
    serializer_class=MovieSerializer


class ActionViewSet(viewsets.ModelViewSet):
    queryset=Moviedata.objects.filter(genre='action') #in the video genre is typ
    serializer_class=MovieSerializer


class ComedyViewSet(viewsets.ModelViewSet):
    queryset=Moviedata.objects.filter(genre='comedy') #in the video genre is typ
    serializer_class=MovieSerializer

