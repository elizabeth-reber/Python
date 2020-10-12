
from django.shortcuts import render, HttpResponse, redirect
#from .models import *
import random

# Create your views here.
def index(request):
    #show all shows in DB
    context = {
    'all_shows': Show.objects.all()
    }
    return render(request, "index.html") 

def create_form(request):
    #show a form to create a Show
    return render(request, 'create.html')

def create_show(request):
    #create an instance of the Dog class
    if request.method == "POST":
        print(request.POST)
        show.objects.create(name=request.POST['show_name'])
    return redirect('/')

def show_show(request, id):
    #show one instance of a show on a template
    context = {
        "one_show": show.objects.get(id=id)
    }
    return render(request, 'one_show.html', context)

def delete_show(request, id):
    #delete a show from the database
    if request.method == "POST":
        show_to_delete = show.objects.get(id=id)
        show_to_delete.delete()
    return redirect('/')

def edit_show(request, id):
    #show a form to edit a show instance
    context = {
        "one_show": show.objects.get(id=id)
    }
    return render(request, "one_show_edit.html", context)

def update_show(request, id): 
    #update the single show in the database and save
    if request.method == "POST":
        show_to_update = show.objects.get(id=id)
        show_to_update.name = request.POST['show_name']
        show_to_update.save()
    return redirect('/shows/' + id)
