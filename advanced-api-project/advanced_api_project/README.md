# API Endpoints Documentation

## Books API

### 1. List Books
- **GET /api/books/**: Retrieve a list of all books.
  - Accessible by all users (read-only).

### 2. Create Book
- **POST /api/books/**: Create a new book.
  - Requires authentication (only authenticated users can create books).

### 3. Retrieve Book Details
- **GET /api/books/{id}/**: Retrieve a book by its ID.
  - Accessible by all users (read-only).

### 4. Update Book
- **PUT /api/books/{id}/**: Update an existing book by ID.
  - Requires authentication (only authenticated users can update).

### 5. Delete Book
- **DELETE /api/books/{id}/**: Delete a book by ID.
  - Requires authentication (only authenticated users can delete).
