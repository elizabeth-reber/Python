from django.db import models

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Authors(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    notes=models.Chield(max_length=255)
    books = models.ManyToManyField(Books, related_name='authors')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# class Books_authors(models.Model):
    # books = models.ForeignKey(Books, related_name='books_authors', on_delete=models.CASCADE)
    # authors = models.ForeignKey(Authors, related_name='books_authors', on_delete=models.CASCADE)

