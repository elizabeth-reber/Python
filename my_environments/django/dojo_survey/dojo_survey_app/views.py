from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return HttpResponse("good to go")

def dashboard(request):
    return HttpResponse("place dashboard")

def user_page(request, id):
    return HttpResponse('place where user ' + str(id) + " 's page is")

def firstTemplate(request):
    context = {
        'name': "Bob Smith",
        'email': 'bob@gmail.com'
    }
    return render(request, "index.html", context)

def submission(request):
    #context = {
        #"name_from_form" : request.POST['user_name']
        #"secret_from_form": request.POST['secret']
        #"fav_character": request.POST['fav_character']
    #}
    request.session['user_name'] = request.POST['user_name']
    request.session['secret'] = request.POST['secret']
    request.session['fav_character'] = request.POST['fav_character']
    print(request.POST)
    return redirect("/thank_you")

def thank_you(request):
    #context = {
    #    "name_from_form" : request.session['user_name']
    #    "secret_from_form": request.session['secret']
    #   "fav_character": request.session['fav_character']
    #}
    return render(request, "thank_you.html")
