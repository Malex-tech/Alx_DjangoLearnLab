from rest_framework import serializers
from datetime import datetime
from .models import Author, Book
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    publication_year = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = '__all__'

    def get_publication_year(self, obj):
        return obj.published_date.year if obj.published_date else None

class BookSerializer(serializers.ModelSerializer):
    """
    Serializes all fields of the Book model.
    Includes custom validation to ensure publication_year is not in the future.
    """
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']  # Explicitly list fields

    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializes the Author model with a nested list of their books.
    Books can also be created or updated through this serializer.
    """
    books = BookSerializer(many=True)
    books = BookSerializer(many=True, read_only=True)


    class Meta:
        model = Author
        fields = ['id', 'name', 'books']

    def create(self, validated_data):
        """
        Create Author and nested Books.
        """
        books_data = validated_data.pop('books', [])
        author = Author.objects.create(**validated_data)

        for book_data in books_data:
            Book.objects.create(author=author, **book_data)

        return author

    def update(self, instance, validated_data):
        """
        Update Author and nested Books.
        If books data is provided, replace all existing books for this author.
        """
        books_data = validated_data.pop('books', None)

        instance.name = validated_data.get('name', instance.name)
        instance.save()

        if books_data is not None:
            # Remove old books and add new ones
            instance.books.all().delete()
            for book_data in books_data:
                Book.objects.create(author=instance, **book_data)

        return instance
