from django.db import models

class Film(models.Model):
    name = models.TextField(max_length=100)
    duration = models.IntegerField()
    country = models.TextField(max_length=100)
    gender = models.TextField(max_length=100)
    ##release = models.DateField(auto_now=False, auto_now_add=False)
    producers = models.TextField(max_length=400)
    description = models.TextField()
    img = models.TextField()

    def __unicode__(self):
        return self.name

class Director(models.Model):
    name = models.TextField(max_length=100)
    surname = models.TextField(max_length=200)

class Actor(models.Model):
    name = models.TextField(max_length=100)
    surname = models.TextField(max_length=200)

class FilmDirectors(models.Model):
    film = models.ForeignKey(Film)
    director = models.ForeignKey(Director)

class FilmActors(models.Model):
    film = models.ForeignKey(Film)
    actor = models.ForeignKey(Actor) 