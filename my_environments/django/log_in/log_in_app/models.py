from __future__ import unicode_literals
from django.db import models
import re 

# Create your models here.
class UserManager(models.Manager):
    def create_validator(self, requestPOST):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(requestPOST['user_name']) <5:
            errors['user_name'] = "Name must be at least 5 characters."
        if len(requestPOST['email']) < 8:
            errors['email'] = "Email needs to be longer."
        if len(reuestPOST["pasword"]) < 8:
            errors['password'] = "passwords must be at least 8 characters"
        if requestPOST['password'] != requestPOST['password_conf']
            errors['password_conf'] = "Password and and password conf need to match." 
        if not EMAIL_REGEX.match(requestPOST['email']):
            errors['regex'] = "Email is not in correct format."
        return errors

class User(models.Model):
    name= models.CharField(max_length=40)
    email = models.CharField(max_length=50)
    password = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()