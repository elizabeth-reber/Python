from django.shortcuts import render, HttpResponse, redirect
from .models import Show
from django.contrib import messages

def index(request):
    shows = Show.objects.all()
    context = dict(shows=shows)
    return render(request, 'shows.html', context)
    
def edit(request, show_id):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/shows/{show_info}/edit')
    context = {
        'show': Show.objects.get(id=show_id)
    }
    return render(request, 'edit.html', context)

def show(request, show_id):    
    context = {
        'show_info': Show.objects.get(id=show_id)
    }
    return render(request, 'show.html', context)

def create(request):
    if request.method == "POST":
        print("it's working")
        errors = Show.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                print(value)
                messages.error(request, value)
            return redirect('/create')
        title=request.POST.get("title")
        network=request.POST.get("network")
        description=request.POST.get("description")
        release_date=request.POST.get("release_date")
        print(release_date)
        show=Show.objects.create(title=title, network=network, description=description, release_date=release_date)
        #return render(request, 'show.html', dict(show=show))
        return redirect(f'/{show.id}')
    return render(request, 'new.html')

def delete(request, show_id):
    to_delete = Show.objects.get(id=show_id)
    to_delete.delete()
    return redirect('/shows')

def update(request, show_id):
    to_update = show.object.get(id=show_id)
    to_update.title = request.POST['title']
    to_update.release_date = request.POST['release_date']
    to_update.network = request.POST['network']
    to_update.description = request.POST['description']
    return redirect('/shows/')
