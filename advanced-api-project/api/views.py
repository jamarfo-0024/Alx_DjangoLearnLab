from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Book
from .serializers import BookSerializer



# ======================================================
# Book List View
# ======================================================
# Purpose:
# - Retrieve all books
# - Supports filtering, searching, and ordering
# - Accessible to all users (read-only)
#
class BookListView(generics.ListAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]

    # Filtering + Searching + Ordering
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]

    # Filtering fields
    filterset_fields = ['title', 'author', 'publication_year']

    # Search functionality
    search_fields = ['title', 'author__name']

    # Ordering functionality
    ordering_fields = ['title', 'publication_year']

    # Default ordering
    ordering = ['title']


# ======================================================
# Book Detail View
# ======================================================
# Purpose:
# Retrieve single book by ID
#
class BookDetailView(generics.RetrieveAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]


# ======================================================
# Book Create View
# ======================================================
# Purpose:
# Create new book
# Only authenticated users allowed
#
class BookCreateView(generics.CreateAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    # Custom create behavior hook
    def perform_create(self, serializer):
        serializer.save()


# ======================================================
# Book Update View
# ======================================================
# Purpose:
# Update existing book
# Only authenticated users allowed
#
class BookUpdateView(generics.UpdateAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save()


# ======================================================
# Book Delete View
# ======================================================
# Purpose:
# Delete book
# Only authenticated users allowed
#
class BookDeleteView(generics.DestroyAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
