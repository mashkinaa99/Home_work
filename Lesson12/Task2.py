class Book:
    number_of_books = 0

    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author

    def __str__(self):
        return f'{self.name}, {self.year}, {self.author}'

    def __repr__(self):
        return f'{self.name}, {self.year}, {self.author}'


class Author:
    books = []

    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday

    def __str__(self):
        return f'{self.name}, {self.country}, {self.birthday}'

    def __repr__(self):
        return f'{self.name}, {self.country}, {self.birthday}'


class Library:
    books = []
    authors = []
    name = 'Feather'

    def new_book(self, name: str, year: int, author: Author):
        book = []
        info_book = Book(name, year, author)
        book.append(info_book)
        self.books.append(book)
        Book.number_of_books += 1

    def group_by_author(self, author: Author):
        i = 0
        while i < len(self.books):
            if author == self.books[i][0].author:
                Author.books.append(self.books[i])
                i += 1
            else:
                i += 1
        return Author.books

    def group_by_year(self, year: int):
        group_books = []
        i = 0
        while i < len(self.books):
            if year == self.books[i][0].year:
                group_books.append(self.books[i])
                i += 1
            else:
                i += 1
        return group_books

    def __str__(self):
        return self.books

    def __repr__(self):
        return self.books


a = Author('Alena Kalashnikova', 'Kyiv', '12.02.1999')
a2 = Author('Artem Kalashnikov', 'Kyiv', '27.02.1997')

lib = Library()

lib.new_book('Life outside the computer', 2019, a)
lib.new_book('Sunny weather', 2021, a)
lib.new_book('Yorkshire Terrier', 2019, a)
lib.new_book('Vacation', 2021, a2)

