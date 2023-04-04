from django.shortcuts import render
from django.views.generic import ListView
from .models import *

# Create your views here.


class FilmListView(ListView):
    model = Film
    template_name = 'film.html'
