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
