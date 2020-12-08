from django.db import models

from common.abstracts import TimeStampedModel


class Movie(models.Model):
    name = models.CharField(max_length=255)
    imdbID = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Favorites(TimeStampedModel):
    name = models.CharField(max_length=255)
    movies = models.ManyToManyField(Movie, blank=True, related_name='favorite_lists')

    def __str__(self):
        return self.name
