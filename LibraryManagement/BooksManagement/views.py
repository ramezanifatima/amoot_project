from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, BorrowedBook
from .forms import BookForm, DateBorrowForm
from datetime import datetime


def book_list(request):
    books = Book.objects.all()

    context = {
        'books': books
    }
    return render(request, 'BooksManagement/books_list.html', context)


def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book:book_list')

    else:
        form = BookForm()
    return render(request, 'BooksManagement/book_create.html', {'form': form})


def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book:book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'BooksManagement/book_update.html', {'form': form})


def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect('book:book_list')
    return render(request, 'BooksManagement/book_delete.html', {'book': book})


def borrow_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    user = request.user
    if request.method == 'POST':
        form = DateBorrowForm(request.POST)
        if form.is_valid():
            book.is_available = False
            BorrowedBook.objects.create(user=user, book=book, borrow_date=form.cleaned_data['borrow_date'],
                                        return_date=form.cleaned_data['return_date'])
            book.save()
            return redirect('book:book_list')
    else:
        form = DateBorrowForm()
    return render(request, 'BooksManagement/book_borrow.html', {'form': form})


def list_of_borrowed_books(request):
    user = request.user
    borrowed_book = BorrowedBook.objects.filter(user=user)
    return render(request, 'BooksManagement/list_of_borrowed_book.html', {'borrowed_book': borrowed_book})


def back_borrow(request, pk):
    borrow = get_object_or_404(BorrowedBook, pk=pk)
    book = borrow.book
    if request.method == 'POST':
        book.is_available = True
        borrow.status = False
        borrow.return_date = datetime.now()
        book.save()
        borrow.save()
        return redirect('book:borrowed_list_book')
    return render(request, 'BooksManagement/book_back.html', {'book': book})
