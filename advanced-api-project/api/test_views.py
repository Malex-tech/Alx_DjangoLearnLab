# api/test_views.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Book
from datetime import date

class BookAPITests(APITestCase):

    def setUp(self):
        # Create test users
        self.user = User.objects.create_user(username="testuser", password="testpass123")
        self.admin_user = User.objects.create_superuser(username="admin", password="adminpass123")

        # Create some books
        self.book1 = Book.objects.create(
            title="Things Fall Apart",
            author="Chinua Achebe",
            description="Classic African literature",
            published_date=date(1958, 6, 17)
        )
        self.book2 = Book.objects.create(
            title="Half of a Yellow Sun",
            author="Chimamanda Ngozi Adichie",
            description="Nigerian Civil War novel",
            published_date=date(2006, 9, 12)
        )

        self.client = APIClient()

    def test_list_books(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 2)

    def test_retrieve_book_detail(self):
        url = reverse('book-detail', args=[self.book1.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    def test_create_book_authenticated(self):
        self.client.login(username="testuser", password="testpass123")
        url = reverse('book-create')
        data = {
            "title": "Americanah",
            "author": "Chimamanda Ngozi Adichie",
            "description": "A novel about race and identity",
            "published_date": "2013-05-14"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_unauthenticated(self):
        url = reverse('book-create')
        data = {
            "title": "Test Book",
            "author": "Test Author",
            "description": "Test Description",
            "published_date": "2025-01-01"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book_authenticated(self):
        self.client.login(username="testuser", password="testpass123")
        url = reverse('book-update', args=[self.book1.pk])
        data = {
            "title": "Things Fall Apart - Updated",
            "author": "Chinua Achebe",
            "description": "Updated description",
            "published_date": "1958-06-17"
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Things Fall Apart - Updated")

    def test_delete_book_authenticated(self):
        self.client.login(username="testuser", password="testpass123")
        url = reverse('book-delete', args=[self.book2.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(pk=self.book2.pk).exists())

    def test_filter_books_by_author(self):
        url = reverse('book-list') + "?author=Chimamanda Ngozi Adichie"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for book in response.data:
            self.assertEqual(book['author'], "Chimamanda Ngozi Adichie")

    def test_search_books(self):
        url = reverse('book-list') + "?search=Things"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any("Things" in book['title'] for book in response.data))

    def test_order_books_by_publication_year(self):
        url = reverse('book-list') + "?ordering=publication_year"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book['publication_year'] for book in response.data]
        self.assertEqual(years, sorted(years))
