from rest_framework import serializers
from .models import Movie, Genre
from showtimes.serializers import ShowtimeSerializer  # NUEVO


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)  # YA EXISTÍA
    showtimes = ShowtimeSerializer(many=True, read_only=True)  # NUEVO (related_name='showtimes')

    class Meta:
        model = Movie
        fields = '__all__'  # IMPORTANTE