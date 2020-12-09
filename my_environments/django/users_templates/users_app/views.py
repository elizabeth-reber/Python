from django.shortcuts import render, HttpResponse
from .models import User

def index(request):
    context = {
       "list_of_users": User.objects.all() 
    }
    return render(request, 'index.html', context)
