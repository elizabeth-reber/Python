from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('dogs/new', views.create_form),
    path('dogs/create', views.create_dog),
    path('dogs/<int:id>', views.show_dog),
    path('dogs/<int:id>/destroy', views.delete_dog),
    path('dogs/<init:id>/edit', views.edit_dog),
    path('dogs/<init:id>/update', views.update_dog),	   
]
