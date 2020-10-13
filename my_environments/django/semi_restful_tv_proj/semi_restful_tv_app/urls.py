from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('shows/new', views.create_form),
    path('shows/create', views.create_show),
    path('shows/<int:id>', views.show_show),
    path('shows/<int:id>/destroy', views.delete_show),
    path('shows/<int:id>/edit', views.edit_show),
    path('shows/<int:id>/update', views.update_show),	   
]
