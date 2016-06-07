from rest_framework import serializers
from .models import Film, Director, Actor, FilmDirectors, FilmActors

class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ('id', 'name', 'duration', 'country', 'gender', 'producers', 'description', 'img',)

        def update(self, instance, validated_data):
            
            ## Update and return an existing `Film` instance, given the validated data.

            instance.name = validated_data.get('name', instance.title)
            instance.duration = validated_data.get('duration', instance.code)
            instance.country = validated_data.get('country', instance.linenos)
            instance.gender = validated_data.get('gender', instance.language)
            instance.producers = validated_data.get('producers', instance.style)
            instance.description = validated_data.get('description', instance.style)
            instance.img = validated_data.get('img', instance.style)
            instance.save()
            return instance

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ('id', 'name', 'surname',)

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('id', 'name', 'surname',)

class FilmDirectorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmDirectors
        fields = ('id', 'film', 'director',)

class FilmActorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmActors
        fields = ('id', 'film', 'actor',)
