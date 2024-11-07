# Delete Operation
**Command:**
```python
from bookshelf.models import Book
book.delete()
Book.objects.all()
[]  # Empty QuerySet, confirming deletion
(1, {'bookshelf.Book': 1})