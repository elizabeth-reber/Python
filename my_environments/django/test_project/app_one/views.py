from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

# Create your views here.
def index(request):
    return render(request, 'index.html')

def new(request):
    return render(request, 'new.html')

def create(request):
    print("you created a blog post")
    print(request.POST)
    print(request.post['p_name'])
    print(request.post['b_post'])
    request.session['blog_post'] = request.POST['b_post']
    request.session['first_name'] = request.POST['p_name']
    return redirect('/')

def show(request, number):
    context = {
        'blog_id':number
        'time': strftime("%Y-%m-%d %H:%M %p", gtime()),
        'randy': int(random.random() * 100)
    }
    return render(request, 'one_blog.html', context)

def edit(request, number):
    return HttpResponse(f"This is a placeholder to edit blog: {number}")

def destroy(request, number):
    return HttpResponse(f"This is a placeholder to delete blog: {number}")

def index(request):
    return render(request, "index.html")