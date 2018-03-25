from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)


class Movie(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    director = models.ForeignKey(Person)
    actors = models.ManyToManyField(Person, through='Role', related_name='movie_actors')
    year = models.IntegerField()


class Role(models.Model):
    role_name = models.CharField(max_length=128)
    person = models.ForeignKey(Person)
    movie = models.ForeignKey(Movie)

