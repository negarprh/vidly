from django.db import models

# django.db encapsulated all things about db
# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=255)
