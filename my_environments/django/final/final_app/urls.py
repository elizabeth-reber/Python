from django.urls import path, include   
from . import views  


urlpatterns = [
    path('', views.index),	 
    path('register', views.register),
    path('wall', views.wall),
    path('login', views.login),
    path('logoff', views.logoff),
    path('post_message', views.post_message),
    path('post_comment/<int:wall_comment_id>', views.post_comment),
    
    
]