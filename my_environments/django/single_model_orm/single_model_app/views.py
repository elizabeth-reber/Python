from django.shortcuts import render, HttpResponse, redirect 
from .models import *


# show all of the data from a table
def index(request):
    context = {
    	"all_the_Users": User.objects.all()
    }
    return render(request, "home.html", context)

def create(request):
    new_user = User.objects.create(first_name=request.POST['first_name'],last_name=request.POST["last_name"], email_address = request.POST["email"], age = request.POST["age"])
    print(new_user)
    return redirect('/')



# def login(request):
#     print("Is my method being called")
#     if request.method == 'POST':
#         print("is it a post request?")
#         logged_user = User.objects.filter(email=request.POST['email'])
#         print(logged_user)
#         print(User.objects.all())
#         if len(logged_user) > 0:
#             logged_user = logged_user[0]
#             print(logged_user)
#             print(logged_user.password, request.POST['password'])
#             if logged_user.password == request.POST['password']:
#                 request.session['name'] = logged_user.first_name
#                 return redirect('/success')
#     return redirect('/')