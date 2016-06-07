from django.shortcuts import render
from .models import Film, Director, Actor
from .serializers import FilmSerializer, DirectorSerializer, ActorSerializer
from rest_framework import viewsets

class FilmViewSet(viewsets.ModelViewSet):
 
    serializer_class = FilmSerializer
    queryset = Film.objects.all()

class DirectorViewSet(viewsets.ModelViewSet):
 
    serializer_class = DirectorSerializer
    queryset = Director.objects.all()

class ActorViewSet(viewsets.ModelViewSet):
 
    serializer_class = ActorSerializer
    queryset = Actor.objects.all()
