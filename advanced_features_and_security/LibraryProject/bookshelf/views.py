from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import SearchForm

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()

    if request.GET.get('q'):
        form = SearchForm(request.GET)
        if form.is_valid():
            books = books.filter(title__icontains=form.cleaned_data['q'])
    else:
        form = SearchForm()

    return render(request, 'bookshelf/book_list.html', {'books': books, 'form': form})
