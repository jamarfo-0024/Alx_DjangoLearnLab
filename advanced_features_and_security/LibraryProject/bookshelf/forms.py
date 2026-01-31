from django import forms
from .models import Book

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title']

    # Additional validation for security (avoid malicious input)
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if "<script>" in title.lower():
            raise forms.ValidationError("Invalid input detected.")
        return title
