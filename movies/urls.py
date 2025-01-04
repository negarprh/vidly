from django.urls import path
from . import views

# The empty string in path('') represent the root
# movies /
# movie /1/details

# Url configuration
urlpatterns = [
    path('', views.index, name='index')
]
