
from django.shortcuts import render, HttpResponse, redirect
from .models import *

def index(request):
    context = {
        'list_of_dojos': Dojo.objects.all(),
        'list_of_ninjas': Ninja.objects.all(),
    }
    return render(request, 'index.html', context)

def submission(request):
    # crud command to create the new ninja
    return redirect('/')

