from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie
# Create your views here.


# Index function represent the main page of our app
# the request parameter, the object that passed to this function is an http request object

def index(request):
    # These methods represent our db abstraction api that simplfied a lot of cases
    movies = Movie.objects.all()
    # output = ', '.join([m.title for m in movies])
    return render(request, 'index.html', {'movies': movies})
