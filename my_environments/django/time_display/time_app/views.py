from django.shortcuts import render
from time import gtime, strftime

# Create your views here.

def index(request):
    context = {
        "time": "Current time"
    }
    return render(request, 'index.html', context)

