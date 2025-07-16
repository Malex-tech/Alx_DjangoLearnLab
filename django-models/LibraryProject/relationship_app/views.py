from django.shortcuts import render
from .models import Book, Library
from django.views.generic.detail import DetailView  # for CBV

# Function-Based View to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})

# Class-Based View to display library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
