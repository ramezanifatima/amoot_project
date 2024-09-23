import json
import random


class Book():
    def __init__(self, title, author, shabak, version, status):
        self.title = title
        self.author = author
        self.shabak = shabak
        self.version = version
        self.status = True

    def to_dict(self):
        return {
            'title': self.title,
            'author': self.author,
            'shabak': self.shabak,
            'version': self.version,
            'status': self.status
        }


class Member():
    def __init__(self, name, membership_number, borrowed_book):
        self.name = name
        self.membership_number = membership_number
        self.borrowed_book = borrowed_book

    def to_dict(self):
        return {
            'name': self.name,
            'membership_number': self.membership_number,
            'borrowed_book': self.borrowed_book

        }


class Library():
    def __init__(self, json_books='books.json', json_member='members.json'):
        self.json_book = json_books
        self.json_member = json_member

    def add_book(self):
        print('Please enter the requested information : ')
        t = input('Enter the title of the book')
        a = input('Enter the author of the book')
        s = int(input('Enter the shabak of the book'))
        v = input('Enter the version of the book')
        sta = True
        book = Book(t, a, s, v, sta)
        try:
            with open(self.json_book, 'r') as file:
                books = json.load(file)

        except (FileNotFoundError, json.JSONDecodeError):
            books = []
        book_s = False
        for book in books:
            if book['shabak'] == s:
                print('shabak tekrari ast ')
                book_s = True
        if not book_s:
            books.append(book.to_dict())
            with open(self.json_book, 'w') as file:
                json.dump(books, file)

            print(f'book add')



    def remove_book(self):
        s = int(input('To remove the book, enter shabak : '))
        with open('books.json', 'r') as file:
            books = json.load(file)
        for book in books:
            if book['shabak'] == s:
                books.remove(book)
        with open(self.json_book, 'w') as file:
            json.dump(books, file)
            print('The book was successfully deleted')

    def lend_book(self):
        print('Enter the required information to borrow a book')
        membership_number = int(input('Enter your membership number'))
        name_book = input('Enter the name of the desired book')
        with open('books.json', 'r') as file_book:
            books = json.load(file_book)

        with open('members.json', 'r') as file_members:
            members = json.load(file_members)
        member_found = False
        for member in members:
            if member['membership_number'] == membership_number:
                if 'borrowed_book' not in member:
                    member['borrowed_book'] = []
                if len(member['borrowed_book']) <= 3:
                    print('You cannot take more than 3 books')
                member['borrowed_book'].append(name_book)
                member_found = True
        if not member_found:
            print('member not found')

        book_found = False
        for book in books:
            if book['title'] == name_book and book['status'] == True:
                book['status'] = False
                book_found = True
        if not book_found:
            print('book not found')
        with open(self.json_book, 'w') as file:
            json.dump(books, file)
        with open(self.json_member, 'w') as file:
            json.dump(members, file)
        print('The book was successfully downloaded')

    def list_available_books(self):
        with open('books.json', 'r') as file_book:
            books = json.load(file_book)
            book_available = []
            for book in books:
                if book['status'] == True:
                    book_available.append(book)
        print(f'Books available:\n{book_available}')

li = Library()
try:
    print('Hello, welcome to the libraryTo perform any action, press the corresponding number')
    print('add_book----> 1\nremove_book------>2\nlend_book----->3\nlist_available_books------>4')
    act = int(input('choice action number :  '))
    if act ==1:
        li.add_book()
    elif act == 2:
        li.remove_book()
    elif act == 3:
        li.lend_book()
    elif act == 4:
        li.list_available_books()

except ValueError:
    print('plaess try again ')

