# CRUD Operations for Book Model

## Create Operation
**Command:**
```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

<Book: 1984 by George Orwell>

##Retrieve Operation
**Command:**
'''python
book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)

{<Book: 1984 by George>}

# Update Operation
**Command:**
'''python
book.title = "Nineteen Eighty-Four"
book.save()
<Book: Nineteen Eighty-Four by George Orwell>

# Delete Operation
**Command:**
```python
book.delete()
Book.objects.all()
[]  # Empty QuerySet, confirming deletion
(1, {'bookshelf.Book': 1})