from datetime import date
from typing import List


def validate_isbn(isbn: str) -> str:
    # only numbers?
    clean_isbn = isbn.replace("-", "")
    int(clean_isbn)
    # # check numbers of dashes and their spot
    # splited_isbn = isbn.split("-")
    # # if len(splited_isbn) != 5:
    # #     raise ValueError(f"Format of ISBN:{isbn} is incorrect")
    # # # correct EAN prefix?
    # # if not int(splited_isbn[0]) in (978, 979):
    # #     raise ValueError(f"Prefix of ISBN:{splited_isbn[0]} is incorrect")
    # check digit
    isbn_digit = int(isbn[-1])
    isbn_to_check = 0
    for i in range(0, 12, 2):
        isbn_to_check += int(clean_isbn[i]) + int(clean_isbn[i + 1]) * 3
    if (isbn_digit == isbn_to_check % 10) or (isbn_digit == 10 - (isbn_to_check % 10)):
        pass
    else:
        raise ValueError(f"Check digit of ISBN:{isbn[-1]} is incorrect")
    print("ISBN is correct")
    return isbn


class Book:
    def __init__(self, title: str, author: str, isbn: str):
        self._title = title
        self._author = author
        self._isbn = validate_isbn(isbn)

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def isbn(self):
        return self._isbn

    def __repr__(self):
        return f'{self._author}, "{self._title}"'


class Library:
    def __init__(self):
        self._books_collection = []

    @property
    def books_collection(self):
        return self._books_collection

    def add_book(self, book_to_add: Book) -> None:
        self._books_collection.append({'book': book_to_add,
                                       'status': 'available',
                                       'dates_of_lends': []})

    def search_by_author(self, searched_author: str) -> List:
        if not self._books_collection:
            raise ValueError("Library is empty!")
        else:
            all_book_of_the_author: List = []
            all_book_of_the_author_str = []
            for library_book in self._books_collection:
                if library_book['book'].author == searched_author:
                    all_book_of_the_author.append(library_book["book"])
                    all_book_of_the_author_str.append(f'{library_book["book"]}, status: {library_book["status"]}')
            if not all_book_of_the_author:
                raise ValueError(f"Author: {searched_author} not found")
            else:
                print("\n".join(all_book_of_the_author_str))
                return all_book_of_the_author

    def search_by_title(self, searched_title: str) -> List:
        if not self._books_collection:
            raise ValueError("Library is empty!")
        else:
            all_book_of_the_title = []
            all_book_of_the_title_str = []
            for library_book in self._books_collection:
                if library_book['book'].title == searched_title:
                    all_book_of_the_title.append(library_book["book"])
                    all_book_of_the_title_str.append(f'{library_book["book"]}, status: {library_book["status"]}')
            if not all_book_of_the_title:
                raise ValueError(f"Title: {searched_title} not found")
            else:
                print("\n".join(all_book_of_the_title_str))
                return all_book_of_the_title

    def borrow_book(self, book_to_borrow: Book) -> None:
        if not self._books_collection:
            raise ValueError("Library is empty!")
        for library_book in self._books_collection:
            if library_book['book'] == book_to_borrow:
                library_book['status'] = "lended"
                library_book['dates_of_lends'].append(date.today().strftime("%d/%m/%Y"))


book = Book("LOTR", "J.R.R Tolkien", "978-83-900210-1-0")
book2 = Book("LOTR 2", "J.R.R Tolkien", "978-83-7181-510-2")

my_library = Library()
my_library.add_book(book)
my_library.add_book(book2)
my_library.borrow_book(book)

print(my_library.books_collection)