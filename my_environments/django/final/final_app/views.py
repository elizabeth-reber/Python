from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt

def index(request):
    if 'userid' in request.session:
        user = User.objects.filter(id=request.session['userid'])
        if user:
            return redirect("/quote_dashboard")
    return render(request, 'index.html')

def quote_dashboard(request):
    if 'userid' in request.session:
        user = User.objects.filter(id=request.session['userid'])
        if user:
            context ={
                "user": user[0],
                "wall_messages": Wall_Message.objects.all()
            }
            return render(request, 'quote_dashboard.html', context)
    return redirect('/')

def login(request):
    user = User.objects.filter(email=request.POST['email']) 
    if user: 
        logged_user = user[0] 
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['userid'] = logged_user.id
            return redirect('/quote_dashboard')
    return redirect("/")

def register(request):
    if request.method == "POST":
        errors = User.objects.basic_validator(request.POST)
    if User.objects.filter(email = request.POST['email']):
        messages.error(request, 'Email is already registered')
        return redirect('/')
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()   
        print(pw_hash)      
        new_user = User.objects.create(
            first_name=request.POST['first_name'], 
            last_name=request.POST['last_name'], 
            email=request.POST['email'],  
            password=pw_hash
            ) 
        request.session['userid'] = new_user.id
        messages.success(request, "User successfully created")
        return redirect("/quote_dashboard")   
        messages.success(request, "User successfully created")
        return redirect('/quote_dashboard')
    return redirect('/')

def logoff(request):
    request.session.flush()
    return redirect('/')

def post_message(request):
    if request.method =="POST":
        if 'userid' in request.session:
            user = User.objects.get(id=request.session['userid'])
            Wall_Message.objects.create(
                message=request.POST["post_message"],
                poster=user
            )

    return redirect('/quote_dashboard')

def post_comment(request, wall_comment_id):
    if request.method =="POST":
        if 'userid' in request.session:
            user = User.objects.get(id=request.session['userid'])
            wall_message = Wall_Message.objects.get(id=wall_comment_id)
            Comment.objects.create(
                message=request.POST["post_comment"],
                poster=user,
                wall_message=wall_message
            )
    return redirect('/quote_dashboard')

def delete_comment(request, delete_comment_id):
    if request.method =="POST":
        if 'userid' in request.session:
            user = User.objects.get(id=request.session['userid'])
            delete_message = Comment.objects.get(id=delete_comment_id)
            delete_message.delete()
    return redirect('/quote_dashboard')

def delete_message(request, delete_message_id):
    if request.method =="POST":
        if 'userid' in request.session:
            user = User.objects.get(id=request.session['userid'])
            delete_message = Wall_Message.objects.get(id=delete_message_id)
            delete_message.delete()

    return redirect('/quote_dashboard')

def edit(request):
    if request.method =="POST":
        if 'userid' in request.session:
            user = User.objects.get(id=request.session['userid'])
            edit_user = User.objects.get(id=edit_user)
            edit_user.save()

    return redirect('/edit')

