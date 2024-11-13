# Retrieve Operation
**Command:**
'''python
book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)

{<Book: 1984 by George>}