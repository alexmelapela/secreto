from django.db import models

class Director(models.Model):
    name = models.TextField(max_length=100)
    surname = models.TextField(max_length=200)
    
class Film(models.Model):
    name = models.TextField(max_length=100)
    country = models.TextField(max_length=100)
    year = models.IntegerField()
    duration = models.IntegerField()
    producer = models.TextField(max_length=100)
    gender = models.TextField(max_length=100)
    director = models.ForeignKey(Director)