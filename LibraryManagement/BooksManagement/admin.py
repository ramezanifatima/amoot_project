from django.contrib import admin
from .models import Author, Category, Book, BorrowedBook

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Book)
admin.site.register(BorrowedBook)
