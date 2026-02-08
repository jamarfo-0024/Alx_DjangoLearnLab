from django.db import models


# =====================================================
# Author Model
# =====================================================
# Purpose:
# Represents a book author.
# One Author can have many Books (One-to-Many relationship).
#
# Relationship:
# Author --> Book
# An author may publish multiple books.
#
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# =====================================================
# Book Model
# =====================================================
# Purpose:
# Represents a book written by an author.
#
# Fields:
# - title: name of the book
# - publication_year: year the book was published
# - author: ForeignKey linking each book to one Author
#
# Relationship:
# Many Books belong to one Author.
#
class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()

    # ForeignKey creates one-to-many relationship:
    # One author -> many books
    author = models.ForeignKey(
        Author,
        related_name='books',  # enables reverse lookup
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title
