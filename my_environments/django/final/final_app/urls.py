from django.urls import path, include   
from . import views  


urlpatterns = [
    path('', views.index),	 
    path('register', views.register),
    path('quote_dashboard', views.quote_dashboard),
    path('login', views.login),
    path('logoff', views.logoff),
    path('post_message', views.post_message),
    path('post_comment/<int:wall_comment_id>', views.post_comment),
    path('delete_message/<int:delete_message_id>', views.delete_message),
    path('delete_comment/<int:delete_comment_id>', views.delete_comment),
    path('edit', views.edit)
    
]