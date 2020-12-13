from django.urls import path, include     
from . import views

urlpatterns = [
    path('', views.index), #shows will use this path
    path('<int:show_id>/edit', views.edit),
    path('<int:show_id>', views.show),
    path('create', views.create)   
]
