from src.domain.book import generate_random_books


class BookRepository:
    def __init__(self):
        self._books_data = generate_random_books()

    def books_data_list(self):
        return list(self._books_data.values())

    def __setitem__(self, key, value):
        self._books_data[key] = value

    def __delitem__(self, key):
        del self._books_data[key]

    def __len__(self):
        return len(self._books_data)

    def add_book(self, given_book):
        self._books_data[int(given_book.book_id)] = given_book

    def remove_book(self, book_id):
        del self._books_data[int(book_id)]

    def update_book(self, updated_book):
        self._books_data[updated_book.book_id] = updated_book
