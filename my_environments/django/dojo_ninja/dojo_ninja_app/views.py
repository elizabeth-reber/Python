from django.shortcuts import render, redirect
from .models import *


# Create your views here.
def index(request):
    context = {
        'list_of_dojos': Dojo.objects.all()
    }
    return render(request, 'index.html', context)

def create_dojo(request):
    Dojo.objects.create(
        name=request.POST['name'],
        city=request.POST['city'],
        state=request.POST['state'],
    )
    return redirect('/')

def create_ninja(request):
    Ninja.objects.create(
        first_name=request.POST['first_name'],
        dojo_id=request.POST['dojo'],
    )
    return redirect('/')