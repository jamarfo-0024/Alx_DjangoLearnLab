from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Book
from .serializers import BookSerializer


# ======================================================
# Book List View
# ======================================================
# Purpose:
# - Retrieve all books
# - Allow filtering, search, and ordering
# - Read-only access allowed for all users
#
class BookListView(generics.ListAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Permissions
    permission_classes = [AllowAny]

    # Filtering + Searching + Ordering
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]

    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']


# ======================================================
# Book Detail View
# ======================================================
# Purpose:
# Retrieve a single book by ID
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
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Custom behavior example (optional hook)
    def perform_create(self, serializer):
        # extra logic can be added here
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
    permission_classes = [IsAuthenticatedOrReadOnly]

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
    permission_classes = [IsAuthenticatedOrReadOnly]
