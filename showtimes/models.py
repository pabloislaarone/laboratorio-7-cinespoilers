from django.db import models
from movies.models import Movie


class Showtime(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name='showtimes'  # IMPORTANTE (usado en el serializer)
    )
    start_time = models.DateTimeField()
    room = models.CharField(max_length=50)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f"{self.movie.title} - {self.start_time}"