from django.urls import path, include     
from . import views

urlpatterns = [
    path('', views.index), 
    path('<int:show_id>/edit', views.edit),
    path('<int:show_id>', views.show),
    path('create', views.create),
    path('<int:show_id>/delete', views.delete),  
    path('<int:show_id>', views.update) 
]
