from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'username', 'date_of_birth', 'profile_photo')
