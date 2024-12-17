from django.db import models

# Create your models here.

class Author(models.Model):
    # Author model to store the name of the author 
    name = models.CharField(max_length=100)
 # String representation of the Author
    def __str__(self):
        return self.name

class Book(models.Model):
 # Book model to store the title, publication year, and associated author   
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
     # Foreign key relationship to Author
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title
