from django import forms
from .models import Book  # Replace with your actual model

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']  # Customize as needed