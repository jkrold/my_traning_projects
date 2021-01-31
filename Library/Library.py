from datetime import date
from typing import List

from my_traning_projects.Library.book import Book


class BookLibrary:
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
                library_book['status'] = "lent"
                library_book['dates_of_lends'].append(date.today().strftime("%d/%m/%Y"))
