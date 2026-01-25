from django.shortcuts import render
from .models import Book
from .forms import ExampleForm

def book_list(request):
    books = Book.objects.all()  # safe ORM query (prevents SQL injection)
    return render(request, 'bookshelf/book_list.html', {'books': books})

def example_form_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            form.save()  # safe ORM save
    else:
        form = ExampleForm()

    return render(request, 'bookshelf/form_example.html', {'form': form})
