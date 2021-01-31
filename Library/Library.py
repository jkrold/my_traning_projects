from datetime import date, timedelta
from typing import List

from my_traning_projects.Library.book import Book


class BookLibrary:
    def __init__(self):
        self._books_collection = []
        self._time_to_return_the_book = 14

    @property
    def books_collection(self):
        return self._books_collection

    def add_book(self, book_to_add: Book) -> None:
        self._books_collection.append({'book': book_to_add,
                                       'status': 'available',
                                       'dates_of_lends': [],
                                       'delivery_date': ''})

    def search_by_author(self, searched_author: str) -> List:
        if not self._books_collection:
            raise ValueError("Library is empty!")
        else:
            all_book_of_the_author: List = []
            all_book_of_the_author_str = []
            i = 0
            for library_book in self._books_collection:
                if library_book['book'].author == searched_author:
                    i += 1
                    all_book_of_the_author.append(library_book["book"])
                    if library_book["status"] == 'available':
                        all_book_of_the_author_str.append(f'{i}. {library_book["book"]}, '
                                                          f'status: {library_book["status"]}')
                    else:
                        all_book_of_the_author_str.append(
                            f'{i}. {library_book["book"]}, '
                            f'status: {library_book["status"]} to {library_book["delivery_date"]}')
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
            i = 0
            for library_book in self._books_collection:
                if library_book['book'].title == searched_title:
                    i += 1
                    all_book_of_the_title.append(library_book["book"])
                    if library_book["status"] == 'available':
                        all_book_of_the_title_str.append(f'{i}. {library_book["book"]}, '
                                                         f'status: {library_book["status"]}')
                    else:
                        all_book_of_the_title_str.append(
                            f'{i}. {library_book["book"]}, '
                            f'status: {library_book["status"]} to {library_book["delivery_date"]}')
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
                if library_book['status'] == 'available':
                    library_book['status'] = 'lent'
                    date_of_borrow = date.today()
                    date_of_delivery = date_of_borrow + timedelta(self._time_to_return_the_book)
                    library_book['dates_of_lends'].append(date_of_borrow.strftime("%d/%m/%Y"))
                    library_book['delivery_date'] = date_of_delivery.strftime("%d/%m/%Y")
                    print("status changed")
                    return
                else:
                    print("Book is lent!")
        print("Book not found")

if __name__ == '__main__':
    new_library = BookLibrary()
    book1 = Book("Title1", "Author1", "978-83-8008-287-8")
    book2 = Book("Title2", "Author2", "978-83-8008-287-8")
    book3 = Book("Title3", "Author2", "978-83-8008-287-8")
    new_library.add_book(book1)
    new_library.add_book(book2)
    new_library.add_book(book3)
    new_library.borrow_book(book2)
    # print(new_library.books_collection)
    new_library.search_by_author("Author2")
    new_library.search_by_title("Title2")
