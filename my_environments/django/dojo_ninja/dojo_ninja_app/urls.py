from django.urls import path, include     
from . import views

urlpatterns = [
    path('', views.index),
    path('submit_dojo', views.create_dojo),
    path('submit_ninja', views.create_ninja)	   
]
