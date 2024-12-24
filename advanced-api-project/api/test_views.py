from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Book
from django.contrib.auth.models import User

class BookAPITestCase(TestCase):
    def setUp(self):
        # Create test users
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.client = APIClient()
        
        # Authenticate the user
        self.client.login(username="testuser", password="testpassword")
        
        # Create some Book instances
        self.book1 = Book.objects.create(title="Book One", author="Author One", publication_year=2020)
        self.book2 = Book.objects.create(title="Book Two", author="Author Two", publication_year=2021)
    
    def test_list_books(self):
        response = self.client.get("/api/books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
    
    def test_create_book(self):
        data = {"title": "New Book", "author": "New Author", "publication_year": 2022}
        response = self.client.post("/api/books/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
    
    def test_update_book(self):
        data = {"title": "Updated Book", "author": "Updated Author", "publication_year": 2023}
        response = self.client.put(f"/api/books/{self.book1.id}/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Book")
    
    def test_delete_book(self):
        response = self.client.delete(f"/api
