from src.domain.book import Book
from src.repository.BookRepository import BookRepository
from src.domain.exceptions import FileException
import json


class BookJSONRepository(BookRepository):
    def __init__(self, file_name):
        BookRepository.__init__(self)
        self._file_name = file_name
        self._load_file()

    def _load_file(self):
        try:
            file = open(self._file_name, "r")
        except IOError:
            raise FileException("Error! File not found!")
        try:
            books_list = json.load(file)
            for book in books_list:
                BookRepository.add_book(self, Book(book["book_id"], book["title"], book["author"]))
        except json.JSONDecodeError:
            BookRepository.__init__(self, dict())
        file.close()

    def _list_of_book_dictionaries(self):
        books_list = BookRepository.books_data_list(self)
        books_dictionaries_list = []
        for book in books_list:
            books_dictionaries_list.append(book.object_to_dictionary())
        return books_dictionaries_list

    def _save_file(self):
        books_dictionaries_list = self._list_of_book_dictionaries()
        file = open(self._file_name, "w")
        json.dump(books_dictionaries_list, file)
        file.close()

    def add_book(self, book):
        BookRepository.add_book(self, book)
        self._save_file()

    def remove_book(self, book_id):
        BookRepository.remove_book(self, book_id)
        self._save_file()

    def update_book(self, updated_book):
        BookRepository.update_book(self, updated_book)
        self._save_file()
