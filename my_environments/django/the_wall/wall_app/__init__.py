<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    {% load static %}
    <link rel="stylesheet" href="{% static 'css/style.css' %}">    
    <script src="{% static 'js/script.js' %}"></script>
</head>
<body>
        {% if messages %}
    <ul class="messages">    
        {% for message in messages %}    
            <li {% if message.tags %} class="{{ message.tags }}"{% endif %}>{{ message }}</li>    
        {% endfor %}
    </ul>
    {% endif %}
    <h1>Login and Registration</h1>
    <h2>Register</h2>
    <form action ='/register' method="POST">
        {% csrf_token %}
        <p>First Name <input name='first_name' type='text'></p>
        <p>Last Name <input name='last_name' type='text'></p>
        <p>Email <input name='email' type='text'></p>
        <p>Password <input name='password' type='text'></p>
        <p>Confirm Password <input name='confirm_pw' type='text'></p>
        <button type='submit'>Register</button>
    </form>

    <h2>Login</h2>
    <form action="/login" method="POST">
        {% csrf_token %}
        <p>Email<input type="text" name="email"></p>
        <p>Password<input type="text" name="password"></p>
        <button type='submit'>Login</button>
</body>
</html>