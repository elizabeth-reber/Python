from django.urls import path, include     
from . import views

urlpatterns = [
    path('', views.index),
    path('get_book', views.get_book),
    path('get_author', views.get_author),
    path('add_book', views.add_book),
    path('add_author', views.add_author),
    path('show_author', views.show_author),
    path('show_book', views.show_book),
    path('add_author_page', views.add_author_page),
    path('add_book_page', views.add_book_page)

	   
]

