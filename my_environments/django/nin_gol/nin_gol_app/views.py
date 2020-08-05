from django.shortcuts import render, HttpResponse, redirect
import random


def index(request):
    return render(request, 'home.html')

# Store player data from the form inside session variables, 
# and return redirect to a method that renders game.html
def game(request):
    print(request.POST, 'this is my form object')
    request.session['name'] = request.POST['username']
    request.session['ninja_army'] = 0
    request.session['ninja_icon'] = [ ]
    return redirect('/ninja_battle')

# renders game html
def start_battle(request):
    return render(request, 'game.html')

# Add ninja with a counter
def add(request):
    request.session['ninja_army'] += 1
    request.session['ninja_icon'].append(0)
    return redirect('/start_battle')

#generate random number, fight and return ninja icon
def fight(request):
    randy = int(random.random() * request.session['ninja_army'] * 2)
    if randy > request.session['ninja_army']:
        difference = randy -= difference
        request.session['ninja_army'] -= randy - request.session['ninja_army']
    else:
        difference = request.session['ninja_army'] - randy
        request.session['ninja_army'] += request.session['ninja_army'] - randy
            for num in range(difference):
            request.session['ninja_icon'].append(0)
    return redirect('start_battle')
