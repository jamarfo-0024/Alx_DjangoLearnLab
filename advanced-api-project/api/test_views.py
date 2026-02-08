from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User

from .models import Author, Book


# ======================================================
# Book API Tests
# ======================================================
# Purpose:
# Test CRUD endpoints, filtering, searching,
# ordering and permission enforcement.
#
class BookAPITest(APITestCase):

    def setUp(self):
        """
        Setup test data and user authentication.
        """

        # Create test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

        # Create author
        self.author = Author.objects.create(name="Test Author")

        # Create books
        self.book1 = Book.objects.create(
            title="Alpha Book",
            publication_year=2020,
            author=self.author
        )

        self.book2 = Book.objects.create(
            title="Beta Book",
            publication_year=2022,
            author=self.author
        )

        # URLs
        self.list_url = reverse('book-list')
        self.detail_url = reverse('book-detail', args=[self.book1.id])
        self.create_url = reverse('book-create')
        self.update_url = reverse('book-update', args=[self.book1.id])
        self.delete_url = reverse('book-delete', args=[self.book1.id])

    # ==================================================
    # TEST LIST VIEW
    # ==================================================
    def test_get_all_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    # ==================================================
    # TEST DETAIL VIEW
    # ==================================================
    def test_get_single_book(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Alpha Book")

    # ==================================================
    # TEST CREATE BOOK (AUTH REQUIRED)
    # ==================================================
    def test_create_book_authenticated(self):

        # login user
        self.client.login(username='testuser', password='testpass123')

        data = {
            "title": "New Book",
            "publication_year": 2021,
            "author": self.author.id
        }

        response = self.client.post(self.create_url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_unauthenticated(self):

        data = {
            "title": "Unauthorized Book",
            "publication_year": 2021,
            "author": self.author.id
        }

        response = self.client.post(self.create_url, data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # ==================================================
    # TEST UPDATE BOOK
    # ==================================================
    def test_update_book(self):

        self.client.login(username='testuser', password='testpass123')

        data = {
            "title": "Updated Title",
            "publication_year": 2020,
            "author": self.author.id
        }

        response = self.client.put(self.update_url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Title")

    # ==================================================
    # TEST DELETE BOOK
    # ==================================================
    def test_delete_book(self):

        self.client.login(username='testuser', password='testpass123')

        response = self.client.delete(self.delete_url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    # ==================================================
    # TEST FILTERING
    # ==================================================
    def test_filter_books_by_year(self):

        response = self.client.get(f"{self.list_url}?publication_year=2020")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    # ==================================================
    # TEST SEARCH
    # ==================================================
    def test_search_books(self):

        response = self.client.get(f"{self.list_url}?search=Alpha")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    # ==================================================
    # TEST ORDERING
    # ==================================================
    def test_order_books(self):

        response = self.client.get(f"{self.list_url}?ordering=publication_year")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data[0]['publication_year'] <= response.data[1]['publication_year'])
