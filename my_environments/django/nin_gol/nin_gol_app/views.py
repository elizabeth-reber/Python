from django.shortcuts import render, HttpResponse, redirect
import random


def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = []
    return render(request, 'index.html')

def process_money(request):
    print("The form has been submitted!")
    print(request.POST)
    if request.POST['building'] == 'farm':
        num = random.randint(10,21)
        request.session['gold'] += random.randint(10,21)
        request.session['activities'].append("you earned " + str(num) + "Yay!")
    elif request.POST['building'] == 'cave':
        num = random.randint(5,11)
        request.session['gold'] += random.randint(5,11)
        request.session['activities'].append("you earned " + str(num) + "Yay!")
    elif request.POST['building'] == 'house':
        num = random.randint(2,6)
        request.session['gold'] += random.randint(2,6)
        request.session['activities'].append("you earned " + str(num) + "Yay!")
    elif request.POST['building'] == 'casino':
        num = random.randint(-50,51)
        request.session['gold'] += random.randint(-50,51)
        if num > 0:
            request.session['activities'].append("you earned " + str(num) + "Yay!")
        elif num == 0:
            request.session['activities'].append("you earned nothing!")  
        else:
            request.session['activities'].append("you lost " + str(num) + "! BOOOOOO!")
    return redirect('/')

def reset(request):
    request.session.flush()
    return redirect('/')


