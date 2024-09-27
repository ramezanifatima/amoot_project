from django import forms
from .models import Book, BorrowedBook


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'summary',
                  'isbn', 'author', 'category']


class DateBorrowForm(forms.ModelForm):
    class Meta:
        model = BorrowedBook
        fields = ['borrow_date', 'return_date']
