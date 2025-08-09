from django.db import models
from datetime import datetime

class Author(models.Model):
    """
    Author model — represents an individual who has written one or more books.
    One author can have many books (One-to-Many relationship).
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book model — represents a single published work by an author.
    Linked to an Author via ForeignKey (many books → one author).
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books'  # Enables reverse access: author.books.all()
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
