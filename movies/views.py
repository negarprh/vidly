from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


# Index function represent the main page of our app
# the request parameter, the object that passed to this function is an http request object

def index(request):
    return HttpResponse("Hello World")
