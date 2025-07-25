from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect
from .models import Book

@permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
    # your logic to add a book
    return render(request, 'bookshelf/add_book.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    # your logic to edit a book
    return render(request, 'bookshelf/edit_book.html')

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    # your logic to delete a book
    return redirect('book_list')

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

# Create your views here.
# BAD
# Book.objects.raw(f"SELECT * FROM books WHERE title = '{title}'")

# GOOD
title = request.GET.get('title')
books = Book.objects.filter(title__icontains=title)  # ORM handles injection risks

# bookshelf/views.py

from django.http import HttpResponse

def secure_view(request):
    response = HttpResponse("Secure!")
    response['Content-Security-Policy'] = "default-src 'self'"
    return response
