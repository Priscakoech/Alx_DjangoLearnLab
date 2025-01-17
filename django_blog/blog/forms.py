from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post
from .models import Comment
from taggit.forms import TagField

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class Postform(forms.ModelForm):
    tags = TagField(required=False)
    class Meta:
        model = Post
        fields = ['title', 'content', 'Tags']
        widgets = {
            'tags': TagWidget(),
        }
        
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
    
    def clean_content(self):
        content = self.cleaned_data.get('content')
        if not content:
            raise forms.ValidationError("Comment content cannot be empty.")
        return content
    
    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) < 5:
            raise forms.ValidationError("Your comment is too short. Please write at least 5 characters.")
        return content
      
        
        
