from django.contrib import admin

# Register your models here.
<!DOCTYPE html>
  <html>
    <head>
      <meta charset="utf-8">
      <title>Index</title>
      {% load static %}
      <link rel="stylesheet" href="{% static 'style.css' %}">    
      <script src="{% static 'js/script.js' %}"></script>
    </head>
    <body>
    	<img src="{% static 'images/image.jpg' %}" />
    </body>