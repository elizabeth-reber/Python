from django.urls import path, include   
from . import views  


urlpatterns = [
    path('', views.index),	 
    path('register', views.register),
    path('wall', views.wall),
    path('login', views.login),
    
]