from django.shortcuts import render, redirect
from .models import *


# Create your views here.
def index(request):
    context = {
        "add_author": Author.objects.all(),
        "add_book": Book.objects.all()
    }
    return render(request, 'index.html', context)

def add_author(request):
    Author.objects.create(name=request.POST['author'])
    return redirect('/show_author')

def add_author_page(request):
    return render(request, 'add_author.html')

def add_book(request):
    Book.objects.create(title=request.POST['book'])
    return redirect('/add_book')

def add_book_page(request):
    return render(request, "add_book.html")

def show_book(request):
    context = {
        "show_book": Book.objects.all()
    }
    return render(request, 'show_book.html', context)
        

def show_author(request):
    context = {
        "show_author": Author.objects.all()
        }
    return render(request, 'show_author.html', context)

def get_book(request):
    return render(request, 'get_book.html')

def get_author(request):
    return render(request, 'get_author.html')



