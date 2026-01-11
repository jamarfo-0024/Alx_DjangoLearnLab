from bookshelf.models import Book

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
