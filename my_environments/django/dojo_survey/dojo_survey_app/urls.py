from django.urls import path
from . import views 
urlpatterns = [
	path('', views.index),
	path('dashboard', views.dashboard),
	# path('user/<int>'),
	path('firsttemplate', views.firstTemplate),
	path('submission', views.submission),
	path('thank_you', views.thank_you)
]
