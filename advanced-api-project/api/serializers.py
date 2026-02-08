from rest_framework import serializers
from datetime import datetime
from .models import Author, Book


# =====================================================
# BookSerializer
# =====================================================
# Purpose:
# Serializes Book model fields.
#
# Includes custom validation:
# Ensures publication_year is NOT in the future.
#
class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'

    # Custom validation method
    def validate_publication_year(self, value):
        current_year = datetime.now().year

        if value > current_year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )
        return value


# =====================================================
# AuthorSerializer
# =====================================================
# Purpose:
# Serializes Author data including nested books.
#
# Relationship Handling:
# Uses nested BookSerializer to dynamically include
# all books related to the author using the related_name 'books'.
#
class AuthorSerializer(serializers.ModelSerializer):

    # Nested serializer
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
