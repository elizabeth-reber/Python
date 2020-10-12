from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('reset', views.reset),
    path('process_money', views.process_money),
    # path('battle', views.battle),
    # path('add_ninja', views.add),
    # path('fight', views.fight)
]