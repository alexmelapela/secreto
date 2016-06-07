from django.shortcuts import render
from .models import Film, Director, Actor, FilmDirectors, FilmActors
from .serializers import FilmSerializer, DirectorSerializer, ActorSerializer, FilmDirectorsSerializer, FilmActorsSerializer
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
    
class FilmDirectorsViewSet(viewsets.ModelViewSet):
 
    serializer_class = FilmDirectorsSerializer
    queryset = FilmDirectors.objects.all()

class FilmActorsViewSet(viewsets.ModelViewSet):
 
    serializer_class = FilmActorsSerializer
    queryset = FilmActors.objects.all()