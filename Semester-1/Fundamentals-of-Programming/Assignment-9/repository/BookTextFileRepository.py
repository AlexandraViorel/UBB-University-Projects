from src.domain.book import Book
from src.repository.BookRepository import BookRepository
from src.domain.exceptions import FileException


class BookTextFileRepository(BookRepository):
    def __init__(self, file_name):
        BookRepository.__init__(self)
        self._file_name = file_name
        self._load_file()

    def _load_file(self):
        try:
            file = open(self._file_name, "r")
        except IOError:
            raise FileException("Error! File not found!")
        line = file.readline().strip()
        while line != "":
            value = line.split(";")
            book = Book(int(value[0]), value[1], value[2])
            BookRepository.add_book(self, book)
            line = file.readline().strip()
        file.close()

    @staticmethod
    def _book_string(book):
        return str(book.book_id) + ";" + str(book.title) + ";" + str(book.author)

    def _save_file(self):
        file = open(self._file_name, "w")
        books_list = BookRepository.books_data_list(self)
        for book in books_list:
            file.write(self._book_string(book) + "\n")
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
