from rest_framework import serializers
from .models import Book
import datetime
from .models import Author

class Bookserilizer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__' # include all fields of the book model
        
    def validate_publication_year(self, value):
        current_year = datetime.datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("The publication year cannot be in the future.")
        return value
    
class AuthorSerializer(serializers.ModelSerializer):
    books = Bookserilizer(many=True, read_only=True) #Nested serializer for related books
    
    class Meta:
        model = Author
        fields = ['name', 'books'] # include the name and related books