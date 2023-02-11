from src.repository.BookRepository import BookRepository
from src.domain.exceptions import FileException
import pickle


class BookBinaryRepository(BookRepository):
    def __init__(self, file_name):
        BookRepository.__init__(self)
        self._file_name = file_name
        self._load_file()

    def _load_file(self):
        try:
            file = open(self._file_name, "rb")
        except IOError:
            raise FileException("Error! File not found!")
        try:
            books_list = pickle.load(file)
            for book in books_list:
                BookRepository.add_book(self, book)
        except EOFError:
            BookRepository.__init__(self, dict())
        file.close()

    def _save_file(self):
        file = open(self._file_name, "wb")
        books_list = BookRepository.books_data_list(self)
        pickle.dump(books_list, file)
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
