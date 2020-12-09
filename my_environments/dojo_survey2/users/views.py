
from django.shortcuts import render, HttpResponse

def users(request):
    return render(request, 'users.html')

def process(request):
    if request.method == 'POST':
        context = {
            'last_name': request.POST['last_name'],
            'first_name': request.POST['first_name'],
            'email': request.POST['email'],
            'age': request.POST['age'],
        }
    return render(request, 'users.html', context)



