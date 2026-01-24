from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    """
    BookForm uses Django's ModelForm to validate and sanitize user input,
    helping to prevent XSS and SQL injection attacks.
    """
    class Meta:
        model = Book
        fields = ['title', 'author']

        from django import forms
from .models import Book

class ExampleForm(forms.ModelForm):
    """
    ExampleForm demonstrates secure form handling using Django's ModelForm.
    It validates and sanitizes user input to prevent XSS and SQL injection.
    """
    class Meta:
        model = Book
        fields = ['title', 'author']

