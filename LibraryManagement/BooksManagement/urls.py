from .views import book_list, book_create, book_update, book_delete, borrow_book, list_of_borrowed_books, back_borrow
from django.urls import path

app_name = 'book'

urlpatterns = [
    path('', book_list, name='book_list'),
    path('create/book/', book_create, name='book_create'),
    path('update/book/<int:pk>/', book_update, name='book_update'),
    path('delete/book/<int:pk>/', book_delete, name='book_delete'),
    path('borrow/book/<int:pk>/', borrow_book, name='borrow_book'),
    path('borrowed/list', list_of_borrowed_books, name='borrowed_list_book'),
    path('borrowed/back/<int:pk>', back_borrow, name='back_borrow')
]
