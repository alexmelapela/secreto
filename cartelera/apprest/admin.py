from django.contrib import admin

# Register your models here.
from .models import Film
from .models import Director
from .models import Actor

admin.site.register(Film)
admin.site.register(Director)
admin.site.register(Actor)