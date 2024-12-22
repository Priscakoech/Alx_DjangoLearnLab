from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

# Create your views here.
# ListView: Retrieve all books
class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] # allow unauthenticated users to read, but not write
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'author_name', 'publication_year']
    search_fields = ['title', 'author_name']
    ordering_fields = ['title', 'publication_year']
  # retrieve a single book by id  
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticatedOrReadOnly]
  
  # add a new book  
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
  
  # modify an exusting book  
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

#remove a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]