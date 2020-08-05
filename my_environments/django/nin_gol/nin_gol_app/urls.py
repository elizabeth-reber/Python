from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('start_game', views.game),
    path('battle', views.battle)
    path('add_ninja', views.add)
    path('fight', views.fight)
]