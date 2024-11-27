import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    """
    Query all books by a specific author.
    """
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        print(f"Books by {author.name}:")
        for book in books:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"No author found with name {author_name}")

def list_books_in_library(library_name):
    """
    List all books in a library.
    """
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        print(f"Books in {library.name} library:")
        for book in books:
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print(f"No library found with name {library_name}")

def retrieve_librarian_for_library(library_name):
    """
    Retrieve the librarian for a library.
    """
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        print(f"Librarian for {library.name} library: {librarian.name}")
    except Library.DoesNotExist:
        print(f"No library found with name {library_name}")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to {library_name} library")

# Sample calls to the functions
if __name__ == "__main__":
    query_books_by_author("Author Name")  # Replace "Author Name" with an actual author name in the database
    list_books_in_library("Library Name")  # Replace "Library Name" with an actual library name in the database
    retrieve_librarian_for_library("Library Name")  # Replace "Library Name" with an actual library name in the database
