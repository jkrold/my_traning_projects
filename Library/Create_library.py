from my_traning_projects.Library.Library import BookLibrary
from my_traning_projects.Library.book import Book


def get_data():
    with open('database.txt') as data:
        split_data = []
        for i, line in enumerate(data):
            split_line = line.split('\t')
            split_line[2] = split_line[2][:-1]
            split_data.append(split_line)
    return split_data

list_of_books = get_data()
my_library = BookLibrary()
for book_to_add in list_of_books:
    my_library.add_book(Book(book_to_add[0], book_to_add[1], book_to_add[2]))
