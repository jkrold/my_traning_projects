from datetime import date, timedelta

def validate_isbn(isbn: str) -> str:
    # only numbers?
    clean_isbn = isbn.replace("-", "")
    int(clean_isbn)
    # check numbers of dashes and their spot
    split_isbn = isbn.split("-")
    if len(split_isbn) != 5:
        raise ValueError(f"Format of ISBN:{isbn} is incorrect")
    # correct EAN prefix?
    if not int(split_isbn[0]) in (978, 979):
        raise ValueError(f"Prefix of ISBN:{split_isbn[0]} is incorrect")
    # check digit
    isbn_digit = int(isbn[-1])
    isbn_to_check = 0
    for i in range(0, 12, 2):
        isbn_to_check += int(clean_isbn[i]) + int(clean_isbn[i + 1]) * 3
    if (isbn_digit == isbn_to_check % 10) or (isbn_digit == 10 - (isbn_to_check % 10)):
        pass
    else:
        raise ValueError(f"Check digit of ISBN:{isbn[-1]} is incorrect")
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

class Book_item(Book):
    def __init__(self, title: str, author: str, isbn: str):
        super().__init__(title, author, isbn)
        self._available = True
        self._dates_of_lend_and_return = []

    def lend_book(self, lend_date: date = date.today(), rental_time: int = 14) -> str:
        if self._available:
            self._dates_of_lend_and_return.append((lend_date, lend_date + timedelta(rental_time)))
            self._available = False
            return "Book correctly lent"
        else:
            raise AssertionError("Book is lend!")

    def book_return(self) -> str:
        if self._available:
            raise AssertionError("Book isn't lend!")
        else:
            self._dates_of_lend_and_return[-1] = self._dates_of_lend_and_return[-1][0]
            return "Book correctly return"

    def check_rental_day(self) -> None:
        if self._available:
            return
        else:
            if date.today() <= self._dates_of_lend_and_return[-1][1]:
                return
            else:
                raise ValueError("The return date is exceeded!")

    @property
    def available(self):
        return self._available

    @property
    def dates_of_lend_and_return(self):
        return self._dates_of_lend_and_return

