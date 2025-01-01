# Authentication System Documentation

## Overview
The authentication system includes user registration, login, logout, and profile management functionalities. The system uses Django's built-in authentication framework with customizations to suit the blog's requirements.

---

## Custom User Creation Form

### Purpose
The `CustomUserCreationForm` extends Django's `UserCreationForm` to include an email field, making user registration more detailed and user-friendly.

### Location
Defined in: `blog/forms.py`

### Implementation
```python
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
