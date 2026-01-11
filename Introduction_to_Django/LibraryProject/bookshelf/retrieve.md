from bookshelf.models import Book

b = Book.objects.get(title="1984")
b
# Output:
# <Book: 1984>

b.title
# Output: '1984'

b.author
# Output: 'George Orwell'

b.publication_year
# Output: 1949
