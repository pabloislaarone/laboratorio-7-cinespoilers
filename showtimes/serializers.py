from rest_framework import serializers
from .models import Showtime


class ShowtimeSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(source='movie.title', read_only=True)  # NUEVO

    class Meta:
        model = Showtime
        fields = '__all__'  # IMPORTANTE (incluye movie, movie_title, start_time, room)