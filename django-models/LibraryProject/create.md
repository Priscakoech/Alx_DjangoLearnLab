# Create Operation
**Objective:** Create a Book instance with the specified title, author and publication year.
**Command:**
'''python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

<Book: 1984 by George Orwell>