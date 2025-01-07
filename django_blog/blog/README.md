# Django Blog Project

## 📖 Project Overview
This is a Django-powered blog application that allows users to create, read, update, and delete (CRUD) blog posts. The project demonstrates core features of Django, including authentication, permissions, and class-based views, making it a robust example of a dynamic content management system.

---

## 🎯 Features
- **Authentication System**
  - User registration, login, and logout.
  - Only authenticated users can create, edit, and delete posts.
- **CRUD Operations**
  - Create, read, update, and delete blog posts.
  - Posts are displayed in reverse chronological order.
- **Permissions**
  - Only post authors can edit or delete their own posts.
  - List and detail views are accessible to all users.
- **User-Friendly Templates**
  - Styled templates for listing, viewing, creating, editing, and

# Blog Application

This blog application is built with Django and supports creating, editing, and managing blog posts. The app includes features like tagging and searching to enhance user experience and make content easily discoverable.

---

## Features

- **Post Management**: Create, edit, and delete blog posts.
- **Tagging System**: Assign tags to posts for easy categorization.
- **Search Functionality**: Search for posts by title, content, or tags.
- **User Authentication**: Secure login and registration.

---

## Tagging Posts

### Adding Tags
1. When creating or editing a post, use the **Tags** field to add tags.
2. Enter one or more tags separated by commas (e.g., `Django, Python, Web Development`).
3. Save the post, and the tags will be associated with it.

### Viewing Posts by Tag
- Tags are displayed below the post title on the post detail page.
- Clicking on a tag will redirect you to a page listing all posts with the same tag.

### Example
- If you add the tags `Python` and `Django` to a post titled *"Getting Started with Django"*, those tags will appear under the post. Clicking on `Django` will display all posts tagged with `Django`.

---

## Searching for Posts

### Using the Search Bar
1. Enter a keyword in the **Search** field (found on the homepage or navigation bar).
2. Click the **Search** button or press `Enter`.
3. View the search results page, which lists all posts matching your query.

### Search Parameters
- **Title**: Searches for posts with matching keywords in the title.
- **Content**: Searches for posts with matching keywords in the content.
- **Tags**: Searches for posts with matching tags.

### Example
- Searching for the term `Django` will return all posts where `Django` appears in the title, content, or tags.

### Viewing Posts by Specific Tags
- Clicking on a tag will filter posts by that tag without needing to use the search bar.

---

## URL Patterns for Tagging and Search

### Tagging
- URL: `/t
