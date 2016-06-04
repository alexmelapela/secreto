from rest_framework import serializers
from .models import Film, Director

class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ('id', 'name', 'country', 'year', 'duration', 'producer', 'gender', 'director',)

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ('id', 'name', 'surname',)
