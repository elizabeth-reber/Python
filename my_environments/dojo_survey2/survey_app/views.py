
from django.shortcuts import render, HttpResponse

def form(request):
    return render(request, 'form.html')

def process(request):
    if request.method == 'POST':
        context = {
            'name': request.POST['name'],
            'lang': request.POST['language'],
            'loc': request.POST['location'],
        }
    return render(request, 'results.html')