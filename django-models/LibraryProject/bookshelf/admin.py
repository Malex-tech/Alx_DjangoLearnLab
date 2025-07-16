from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # shows these in admin list view
    search_fields = ('title', 'author')                     # makes title and author searchable
    list_filter = ('publication_year',)                     # adds a filter sidebar

admin.site.register(Book, BookAdmin)

# Register your models here.
