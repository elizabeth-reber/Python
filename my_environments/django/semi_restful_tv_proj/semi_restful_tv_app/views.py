
from django.shortcuts import render, HttpResponse, redirect
#from .models import *
import random

# Create your views here.
def index(request):
    #show all dogs in DB
    context = {
    'all_dogs': Dog.objects.all()
    }
    return render(request, "index.html") 

def create_form(request):
    #show a form to create a Dog
    return render(request, 'create.html')

def create_dog(request):
    #create an instance of the Dog class
    if request.method == "POST":
        print(request.POST)
        dog.objects.create(name=request.POST['dog_name'], age=request.POST['age'])
    return redirect('/')

def show_dog(request, id):
    #show one instance of a dog on a template
    context = {
        "one_dog": Dog.objects.get(id=id)
    }
    return render(request, 'one_dog.html', context)

def delete_dog(request, id):
    #delete a dog from the database
    if request.method == "POST":
        dog_to_delete = Dog.objects.get(id=id)
        dog_to_delete.delete()
    return redirect('/')

def edit_dog(request, id):
    #show a form to edit a Dog instance
    context = {
        "one_dog": Dog.objects.get(id=id)
    }
    return render(request, "one_dog_edit.html", context)

def update_dog(request, id): 
    #update the single Dog in the database and save
    if request.method == "POST":
        dog_to_update = dog.objects.get(id=id)
        dog_to_update.name = request.POST['dog_name']
        dog_to_update.age = request.POST['age']
        dog_to_update.save()
    return redirect('/dogs/' + id)
