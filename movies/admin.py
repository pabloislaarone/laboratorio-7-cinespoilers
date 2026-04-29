from django.contrib import admin
from .models import Movie, Genre  # CAMBIO


@admin.register(Genre)  # NUEVO
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Movie)  # CAMBIO
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'duration', 'created_at')
    search_fields = ('title',)
    filter_horizontal = ('genres',)  # IMPORTANTE