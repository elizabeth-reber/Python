from django.shortcuts import render, HttpResponse, redirect

def index(request):    
    return render(request, 'index.html')
    
def create_user(request):
    request.session['first_name'] = request.POST['First Name']
    request.session['last_name'] = request.POST['Last Name']
    request.session['age'] = request.POST['age']
    request.session['email_address'] = request.POST['email']
    return redirect('/')

