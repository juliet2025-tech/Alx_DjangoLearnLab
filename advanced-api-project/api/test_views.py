
#This test module verifies the functionality of the Book API.

# List and retrieve books
# Create, update, and delete books
# Authentication and permissions
# Filtering, searching, and ordering




from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Book


class BookAPITestCase(APITestCase):

    def setUp(self):
        """
        Set up test data and user
        """
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword"
        )

        self.book1 = Book.objects.create(
            title="Django for Beginners",
            author="William",
            publication_year=2020
        )

        self.book2 = Book.objects.create(
            title="Advanced Django",
            author="Jane",
            publication_year=2023
        )

    # -------------------------
    # READ (LIST)
    # -------------------------
    def test_list_books(self):
        response = self.client.get("/api/books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    # -------------------------
    # READ (DETAIL)
    # -------------------------
    def test_retrieve_single_book(self):
        response = self.client.get(f"/api/books/{self.book1.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Django for Beginners")

    # -------------------------
    # CREATE
    # -------------------------
    def test_create_book_authenticated(self):
        self.client.login(username="testuser", password="testpassword")

        data = {
            "title": "REST APIs with Django",
            "author": "John",
            "publication_year": 2024
        }

        response = self.client.post("/api/books/create/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_unauthenticated(self):
        data = {
            "title": "Unauthorized Book",
            "author": "Hacker",
            "publication_year": 2022
        }

        response = self.client.post("/api/books/create/", data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # -------------------------
    # UPDATE
    # -------------------------
    def test_update_book_authenticated(self):
        self.client.login(username="testuser", password="testpassword")

        data = {
            "title": "Updated Django Book",
            "author": "William",
            "publication_year": 2021
        }

        response = self.client.put(
            f"/api/books/update/{self.book1.id}/",
            data
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Django Book")

    # -------------------------
    # DELETE
    # -------------------------
    def test_delete_book_authenticated(self):
        self.client.login(username="testuser", password="testpassword")

        response = self.client.delete(
            f"/api/books/delete/{self.book1.id}/"
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    # -------------------------
    # FILTERING
    # -------------------------
    def test_filter_books_by_author(self):
        response = self.client.get("/api/books/?author=Jane")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    # -------------------------
    # SEARCHING
    # -------------------------
    def test_search_books(self):
        response = self.client.get("/api/books/?search=Advanced")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    # -------------------------
    # ORDERING
    # -------------------------
    def test_order_books_by_publication_year(self):
        response = self.client.get("/api/books/?ordering=-publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(
            response.data[0]["publication_year"],
            response.data[1]["publication_year"]
        )
