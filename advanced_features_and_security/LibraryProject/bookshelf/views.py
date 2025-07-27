from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect
from .models import Book
from .forms import ExampleForm


def my_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Do something with cleaned data
            return render(request, 'success.html', {'form': form})
    else:
        form = ExampleForm()

    return render(request, 'my_template.html', {'form': form})

from django.views.generic import FormView
from .forms import ExampleForm

class MyFormView(FormView):
    template_name = 'my_template.html'
    form_class = ExampleForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # Access the request object with self.request
        print(self.request.user)
        return super().form_valid(form)


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
def search_books(request):
    title = request.GET.get('title')  # Now it's safe
    books = Book.objects.filter(title__icontains=title) if title else Book.objects.all()

    return render(request, 'books/search_results.html', {'books': books})
    books = Book.objects.filter(title__icontains=title)  

from django.http import HttpResponse

def secure_view(request):
    response = HttpResponse("Secure!")
    response['Content-Security-Policy'] = "default-src 'self'"
    return response
