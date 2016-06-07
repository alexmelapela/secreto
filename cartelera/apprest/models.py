from django.db import models

class Director(models.Model):
    name = models.TextField(max_length=100)
    surname = models.TextField(max_length=200)

class Actor(models.Model):
    name = models.TextField(max_length=100)
    surname = models.TextField(max_length=200)

class Film(models.Model):
    name = models.TextField(max_length=100)
    duration = models.IntegerField()
    country = models.TextField(max_length=100)
    gender = models.TextField(max_length=100)
    release = models.DateField(auto_now=False)
    producers = models.TextField(max_length=400)
    description = models.TextField()
    img = models.TextField()
    directors = models.ManyToManyField(Director, related_name='film')
    actors = models.ManyToManyField(Actor, related_name='film')
