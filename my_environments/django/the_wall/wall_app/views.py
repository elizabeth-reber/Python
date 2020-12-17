from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt

def index(request):  
    return render(request, 'index.html')

def wall(request):
    if 'userid' in request.session:
        user = User.objects.filter(id=request.session['userid'])
        if user:
            context = {
                "user": user[0]
            }
            return render(request, 'wall.html', context)
        return redirect('/')

def login(request):
    user = User.objects.filter(email=request.POST['email']) 
    if user: 
        logged_user = user[0] 
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['userid'] = logged_user.id
            return redirect('/wall')
    return redirect("/")

def register(request):
    if request.method == "POST":
        errors = User.objects.basic_validator(request.POST)
    if User.objects.filter(email = request.POST['email']):
        messages.error(request, 'Email is already registered')
        return redirect('/')
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/')
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()  # create the hash    
        print(pw_hash)      
        new_user = User.objects.create(
            first_name=request.POST['first_name'], 
            last_name=request.POST['last_name'], 
            email=request.POST['email'],  
            password=pw_hash
            ) 
        request.session['userid'] = new_user.id
        messages.success(request, "User successfully created")
        return redirect("/wall")   
        messages.success(request, "User successfully created")
        return redirect('/wall')
    return redirect('/')
