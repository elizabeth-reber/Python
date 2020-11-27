from django.urls import path, include     
from . import views
urlpatterns = [
    path('', views.random_word_app),
    path('random_word', views.random_word_app),
    path('reset', views.reset)	   
]
