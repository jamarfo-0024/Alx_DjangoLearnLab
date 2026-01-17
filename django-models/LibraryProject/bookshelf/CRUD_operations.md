# CREATE
from bookshelf.models import Book

book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)
book
# Output:
# <Book: 1984>

# RETRIEVE
Book.objects.all()
# Output:
# <QuerySet [<Book: 1984>]>

b = Book.objects.first()
b.title
# Output: '1984'
b.author
# Output: 'George Orwell'
b.publication_year
# Output: 1949

# UPDATE
b = Book.objects.get(title="1984")
b.title = "Nineteen Eighty-Four"
b.save()

Book.objects.all()
# Output:
# <QuerySet [<Book: Nineteen Eighty-Four>]>

# DELETE
b = Book.objects.get(title="Nineteen Eighty-Four")
b.delete()
# Output:
# (1, {'bookshelf.Book': 1})

Book.objects.all()
# Output:
# <QuerySet []>
