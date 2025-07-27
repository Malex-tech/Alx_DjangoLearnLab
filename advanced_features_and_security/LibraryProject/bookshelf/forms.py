from django import forms
from .models import Book
# LibraryProject/bookshelf/forms.py

from django import forms

class ExampleForm(forms.Form):
    title = forms.CharField(max_length=100)
    author = forms.CharField(max_length=100)
    publish_date = forms.DateField(widget=forms.SelectDateWidget)


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
