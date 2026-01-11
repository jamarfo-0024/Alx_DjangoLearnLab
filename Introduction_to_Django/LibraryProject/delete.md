from bookshelf.models import Book

b = Book.objects.get(title="Nineteen Eighty-Four")
b.delete()
# Output:
# (1, {'bookshelf.Book': 1})

Book.objects.all()
# Output:
# <QuerySet []>
