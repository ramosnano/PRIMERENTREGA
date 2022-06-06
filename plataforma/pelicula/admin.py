from django.contrib import admin
from pelicula.models import Movie, Genero, Resume

admin.site.register(Movie)
admin.site.register(Genero)
admin.site.register(Resume)