# Integrating the Book Model with Django Admin Interface

## Overview

This document describes the process of integrating the **Book model** into Django's admin interface and customizing the display to manage book data more efficiently.

---

## Step 1: Register the Book Model with the Django Admin

To enable the **Book** model to be managed via the Django admin interface, follow these steps:

1. Open the `admin.py` file located in the `bookshelf` app.
2. Import the `Book` model and register it with the admin site.

### Code:

```python
# bookshelf/admin.py
from django.contrib import admin
from .models import Book

admin.site.register(Book)
