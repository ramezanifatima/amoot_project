from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    name = models.CharField(max_length=100)
    family = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} {self.family}"


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class Book(models.Model):
    title = models.CharField(max_length=100)
    isbn = models.CharField(max_length=17)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    summary = models.TextField()
    category = models.ManyToManyField(Category, related_name='category')
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title}"


class BorrowedBook(models.Model):
    user = models.ForeignKey(User, related_name='user_borrowed', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name='borrowed_book', on_delete=models.CASCADE)
    borrow_date = models.DateTimeField()
    return_date = models.DateField(null=True, blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.book.title}"
