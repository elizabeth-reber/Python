from django.shortcuts import render, HttpResponse, redirect
from .models import Show

def index(request):
    shows = Show.objects.all()
    context = dict(shows=shows)
    return render(request, 'shows.html', context)
    
def edit(request, show_id):
    return render(request, 'edit.html')

def show(request, show_id):
    context = {
        'show_info': Show.objects.get(id=show_id)
    }
    return render(request, 'show.html', context)

def create(request):
    if request.method == "POST":
        title=request.POST.get("title")
        network=request.POST.get("network")
        description=request.POST.get("description")
        release_date=request.POST.get("release_date")
        show=Show.objects.create(title=title, network=network, description=description, release_date=release_date)
        #return render(request, 'show.html', dict(show=show))
        return redirect(f'/{show.id}')
    return render(request, 'new.html')
