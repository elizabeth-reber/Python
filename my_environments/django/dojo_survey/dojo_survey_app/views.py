from django.shortcuts import render, HttpResponse

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
    return HttpResponse("The form has been submitted")