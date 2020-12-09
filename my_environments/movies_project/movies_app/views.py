from django.shortcuts import render, HttpResponse
from .models import Director, Movie

def index(request):
    context = {
        Movie.object.all()
    }
    return render(request, 'index.html', context)
