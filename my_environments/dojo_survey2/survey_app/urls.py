from django.urls import path, include     
from . import views

urlpatterns = [
    path('', views.form),
    path('process', views.process),	   
]

