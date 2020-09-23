from django.urls import path
from . import viewsurlpatterns = [
	path('', views.index),
	path('dashboard', views.dashboard),
	path('user/<int>'),
	path('firsttemplate', views.firstTemplate)
	path('submission', views.submission)
]
