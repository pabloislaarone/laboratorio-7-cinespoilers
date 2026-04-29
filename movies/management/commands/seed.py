from django.core.management.base import BaseCommand
from movies.models import Movie, Genre
from showtimes.models import Showtime  # NUEVO
from datetime import datetime, timedelta
import random


class Command(BaseCommand):
    help = 'Seed database with initial data'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING('Seeding data...'))

        # LIMPIAR
        Showtime.objects.all().delete()
        Movie.objects.all().delete()
        Genre.objects.all().delete()

        # GÉNEROS
        genres = [
            Genre.objects.create(name="Acción"),
            Genre.objects.create(name="Drama"),
            Genre.objects.create(name="Comedia"),
            Genre.objects.create(name="Ciencia ficción"),
        ]

        # PELÍCULAS
        movies = []
        for i in range(1, 6):  # 5 películas
            movie = Movie.objects.create(
                title=f"Película {i}",
                description="Descripción de prueba",
                duration=random.randint(90, 180)
            )
            movie.genres.set(random.sample(genres, 2))
            movies.append(movie)

        # SHOWTIMES
        for movie in movies:
            for j in range(2):  # 2 funciones por película
                Showtime.objects.create(
                    movie=movie,
                    start_time=datetime.now() + timedelta(days=j),
                    room=f"Sala {random.randint(1,5)}"
                )

        self.stdout.write(self.style.SUCCESS('Data seeded successfully!'))