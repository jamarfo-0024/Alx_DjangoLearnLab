from django.shortcuts import render
from .forms import ExampleForm

def form_example_view(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            pass  # do something
    else:
        form = ExampleForm()

    return render(request, 'bookshelf/form_example.html', {'form': form})
