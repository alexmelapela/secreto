from django.shortcuts import render
from .models import Film, Director
from .serializers import FilmSerializer, DirectorSerializer
from rest_framework import viewsets

class FilmViewSet(viewsets.ModelViewSet):
 
    serializer_class = FilmSerializer
    queryset = Film.objects.all()

class DirectorViewSet(viewsets.ModelViewSet):
 
    serializer_class = DirectorSerializer
    queryset = Director.objects.all()