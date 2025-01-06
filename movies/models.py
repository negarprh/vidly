from django.db import models
from django.utils import timezone
# django.db encapsulated all things about db
# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# Why we are drinving Movie class from modele class in django?
# Bc this class has bunch of methods in CRUD
# Then is w want to store a movie ibject in the db, we'll just call one of these methods called 'save'.
# Save method internally take care of generating the right sql statment to update the sql db
# This is called: db abstration api
# so this modele class give us an api ( app programming interface)
# and this api, agets away the complexity of working with a db

class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    number_in_stock = models.IntegerField()
    daily_rate = models.FloatField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
