from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt

# Create your views here.
from django.shortcuts import render, HttpResponse
def index(request):
    return HttpResponse("This is my response!")

def register(request):
    if request.method == "POST"
        errors = User.objects.create_quest.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                message.error(request, value)
        else:
            hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
            print(hashed_pw.decode())
            User.objects.create(name=request.POST['user_name'], email=request.POST['email'], password=hashed_pw)
            return redirect('/main_page')
    return rdirect ('/')

def login(request):
    user = User.objects.filter(email=request.POST['email'])
    if len(user) > 0:
        user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
            request.session['user_id'] = user.id
            return redirect('/main_page')
    messages.error(request, "email or password is incorrect")
    return redirect('/')

def main_page(request):
    if 'user_id' not in request.session:
        messages.error(request, "email or password is incorrect")
        return redirect('/')
    context = {
        'user': User.objects.get(id=request.session{'user_id', context])
    }
    return render(request, "main_page.html", context)

def logout(request):
    request.session.clear()
    return redirect('/')