from django.shortcuts import render
from .models import Book
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views import View
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
# Create your views here.
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

from django.views.generic.detail import DetailView
from .models import Library

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    
class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'
    success_url = reverse_lazy('home')  # Redirect to home or any other page after login

class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'

# Custom Registration View
class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'relationship_app/register.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log the user in after registration
            return redirect('home')  # Redirect to home or a designated page
        return render(request, 'relationship_app/register.html', {'form': form})  
  # views.py


# Function to check if the user is an admin
def is_admin(user):
    return user.userprofile.role == 'Admin'

# Function to check if the user is a librarian
def is_librarian(user):
    return user.userprofile.role == 'Librarian'

# Function to check if the user is a member
def is_member(user):
    return user.userprofile.role == 'Member'

# Admin view - accessible only to users with 'Admin' role
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# Librarian view - accessible only to users with 'Librarian' role
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# Member view - accessible only to users with 'Member' role
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

    