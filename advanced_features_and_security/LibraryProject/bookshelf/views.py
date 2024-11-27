from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseForbidden
from .models import Document

@permission_required('app_name.can_view', raise_exception=True)
def document_list(request):
    documents = Document.objects.all()
    return render(request, 'documents/document_list.html', {'documents': documents})

@permission_required('app_name.can_create', raise_exception=True)
def document_create(request):
    if request.method == 'POST':
        # Handle form submission
        pass
    return render(request, 'documents/document_create.html')

@permission_required('app_name.can_edit', raise_exception=True)
def document_edit(request, pk):
    document = get_object_or_404(Document, pk=pk)
    if request.method == 'POST':
        # Handle form submission
        pass
    return render(request, 'documents/document_edit.html', {'document': document})

@permission_required('app_name.can_delete', raise_exception=True)
def document_delete(request, pk):
    document = get_object_or_404(Document, pk=pk)
    if request.method == 'POST':
        document.delete()
        return redirect('document_list')
    return render(request, 'documents/document_delete.html', {'document': document})
from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book

@permission_required('bookshelf.can_view_books', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})
