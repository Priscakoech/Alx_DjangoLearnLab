from django.db import models

# Create your models here.
# Author model to store author details
class Author(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
# book model to store book details
class Book(models.Model):
    title = models.CharField(max_length=200) # Book's title 
    publication_year = models.IntegerField() # Year of publication
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title