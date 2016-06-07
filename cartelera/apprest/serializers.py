from rest_framework import serializers
from .models import Film, Director, Actor

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ('id', 'name', 'surname',)

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('id', 'name', 'surname',)

class FilmSerializer(serializers.ModelSerializer):
    directors = DirectorSerializer(many = True)
    actors = ActorSerializer(many = True)
    class Meta:
        model = Film
        fields = ('id', 'name', 'duration', 'country', 'gender', 'producers', 'description', 'img', 'directors', 'actors',)