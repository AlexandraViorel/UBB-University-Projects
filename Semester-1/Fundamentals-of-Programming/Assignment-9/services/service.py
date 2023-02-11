from src.repository.BookRepository import BookRepository
from src.repository.ClientRepository import ClientRepository
from src.repository.RentalRepository import RentalRepository
from src.domain.book import Book
from src.domain.client import Client
from src.domain.rental import Rental
from src.domain.rental import BooksWithRentals
from src.domain.rental import AuthorWithRentals
from src.domain.rental import ClientsWithRentalDays
from src.domain.validator import BookValidator
from src.domain.validator import ClientValidator
from src.domain.validator import RentalValidator
from src.domain.exceptions import RepositoryException
from src.domain.exceptions import IdException
from src.domain.exceptions import RentalException
from src.domain.exceptions import UndoRedoException
import datetime
import re
from src.domain.book import generate_random_books
from src.domain.rental import generate_random_rentals
from src.domain.client import generate_random_clients


class UndoRedoObject:
    def __init__(self, undo_function, redo_function):
        self._undo_function = undo_function
        self._redo_function = redo_function

    def undo_function(self):
        self._undo_function()

    def redo_function(self):
        self._redo_function()


class UndoRedoService:
    def __init__(self, book_repository, client_repository, rental_repository):
        self._book_repository = book_repository
        self._client_repository = client_repository
        self._rental_repository = rental_repository
        self._undo_stack = []
        self._undo_pointer = 0

    @property
    def undo_stack(self):
        return self._undo_stack

    def correct_stack(self):
        while len(self._undo_stack) != self._undo_pointer:
            self._undo_stack.pop()

    def add_undo_redo_operations(self, operations_object):
        self.correct_stack()
        self._undo_stack.append(operations_object)
        self._undo_pointer += 1

    def undo(self):
        if self._undo_pointer == 0:
            raise UndoRedoException("There are no operations to undo !")
        self._undo_pointer -= 1
        self._undo_stack[self._undo_pointer].undo_function()

    def redo(self):
        if self._undo_pointer == len(self._undo_stack):
            raise UndoRedoException("There are no operations to redo !")
        self._undo_stack[self._undo_pointer].redo_function()
        self._undo_pointer += 1


class Service:
    def __init__(self, client_repository=None, book_repository=None, rental_repository=None, book_validator=None,
                 client_validator=None, rental_validator=None):
        if book_repository is None:
            book_repository = BookRepository(generate_random_books())
        if client_repository is None:
            client_repository = ClientRepository(generate_random_clients())
        if rental_repository is None:
            rental_repository = RentalRepository(generate_random_rentals())
        if book_validator is None:
            book_validator = BookValidator()
        if client_validator is None:
            client_validator = ClientValidator()
        if rental_validator is None:
            rental_validator = RentalValidator()

        self._book_repository = book_repository
        self._client_repository = client_repository
        self._rental_repository = rental_repository
        self._book_validator = book_validator
        self._client_validator = client_validator
        self._rental_validator = rental_validator
        self._undo_redo_service = UndoRedoService(self._book_repository, self._client_repository, self._rental_repository)

    @property
    def client_repository(self):
        return self._client_repository

    @property
    def book_repository(self):
        return self._book_repository

    @property
    def rental_repository(self):
        return self._rental_repository

    def find_book(self, given_book_id):
        """
            This function searches if a book with the given id exists in the books repository.
        :param given_book_id: the given book id
        :return: true if a book with the same given id exists in the books repository, false if not
        """
        books_list = self.data_from_books_repository()
        for book in books_list:
            current_book_id = book.book_id
            if current_book_id == int(given_book_id):
                return True, book
        return False, None

    def find_client(self, given_client_id):
        """
            This function searches if a client with the given id exists in the clients repository.
        :param given_client_id: the given client id
        :return: ture if a client with the same given id exists in the clients repository, false if not
        """
        clients_list = self.data_from_clients_repository()
        for client in clients_list:
            current_client_id = client.client_id
            if current_client_id == int(given_client_id):
                return True, client
        return False, None

    def is_book_rented(self, given_book_id):
        """
            This function searches if a book with the given id is rented.
        :param given_book_id: the given book id
        :return: true and the rental id if the book is rented, false and None if not
        """
        rentals_list = self.data_from_rentals_repository()
        for rental in rentals_list:
            current_rental_book_id = rental.book_id
            current_rental_return_date = rental.returned_date
            if current_rental_book_id == int(given_book_id) and current_rental_return_date is None:
                return True, rental.rental_id
        return False, None

    def was_book_rented(self, given_book_id):
        """
            This function searches if a book with the given id was rented.
        :param given_book_id: the given book id
        :return: true and the rental id if the book was rented, false and None if not
        """
        rentals_list = self.data_from_rentals_repository()
        for rental in rentals_list:
            current_rental_book_id = rental.book_id
            if current_rental_book_id == int(given_book_id):
                return True, rental.rental_id
        return False, None

    def find_rental(self, given_rental_id):
        """
            This function searches if a rental with the given rental id exists in the rentals repository.
        :param given_rental_id: the given rental id
        :return: true and the rented date if a rental with the same given id exists in the rentals repository, false
        and None if not
        """
        rentals_list = self.data_from_rentals_repository()
        for rental in rentals_list:
            current_rental_id = rental.rental_id
            if current_rental_id == int(given_rental_id):
                return True, rental.rented_date, rental
        return False, None, None

    def client_has_rentals(self, given_client_id):
        """
            This function searches if a client with the given id has a rental.
        :param given_client_id: the given client id
        :return: true and the rental ids list if the client has a rental, false and None if not
        """
        rentals_list = self.data_from_rentals_repository()
        clients_rental_ids_list = []
        for rental in rentals_list:
            current_rental_client_id = rental.client_id
            if current_rental_client_id == int(given_client_id):
                clients_rental_ids_list.append(rental.rental_id)
        if len(clients_rental_ids_list) == 0:
            return False, None
        return True, clients_rental_ids_list

    def return_rental_for_a_given_book(self, given_book_id):
        rentals_list = self.data_from_rentals_repository()
        for rental in rentals_list:
            current_rental_book_id = rental.book_id
            if current_rental_book_id == int(given_book_id):
                return rental

    def create_rentals_list_for_a_given_client(self, given_client_id):
        rentals_list_for_given_client = []
        rentals_list = self.data_from_rentals_repository()
        for rental in rentals_list:
            current_rental_client_id = rental.client_id
            if current_rental_client_id == int(given_client_id):
                rentals_list_for_given_client.append(rental)
        return rentals_list_for_given_client

    # -------------- BOOK SERVICE FUNCTIONS --------------
    def data_from_books_repository(self):
        """
            This function returns a list of all books from the book repository.
        :return: the list of books
        """
        books_list = self._book_repository.books_data_list()
        return books_list

    def add_book(self, book_id, title, author):
        """
            This function adds a book to the book repository.
            - it verifies if the inputs for book id, title and author are correct
            - it verifies if the input for the book id does not already exist in the book repository
        :param book_id: given id
        :param title: given title
        :param author: given name of author
        """
        if not book_id.isnumeric():
            raise IdException("Invalid input for the ID!")
        book = Book(int(book_id), title, author)
        self._book_validator.validate_book(book)
        does_book_exist, book1 = self.find_book(book_id)
        if does_book_exist:
            raise RepositoryException("This book id already exists! ")
        self._undo_redo_service.add_undo_redo_operations(UndoRedoObject(lambda: self.book_repository.remove_book(book_id),
                                                                        lambda: self.book_repository.add_book(book)))
        self._book_repository.add_book(book)

    def remove_book(self, book_id):
        """
            This functions deletes the book with the given id from the book repository.
            - it verifies if the input for book id is correct
            - it verifies if the book exists in the repository
            - it verifies if the book is rented, and it deletes its rental if it's rented
        :param book_id: given id
        """
        if not book_id.isnumeric():
            raise IdException("Invalid input for the ID!")
        does_book_exist, book = self.find_book(book_id)
        if does_book_exist:
            found_book_rental, rental_id = self.was_book_rented(int(book_id))
            if found_book_rental:
                rental = self.return_rental_for_a_given_book(int(book_id))

            def undo_function():
                if found_book_rental:
                    self.rental_repository.add_rental(rental)
                self.book_repository.add_book(book)

            def redo_function():
                if found_book_rental:
                    self.rental_repository.delete_rental(rental_id)
                self.book_repository.remove_book(book_id)

            self._undo_redo_service.add_undo_redo_operations(UndoRedoObject(undo_function, redo_function))
            if found_book_rental:
                self._rental_repository.delete_rental(int(rental_id))
            self._book_repository.remove_book(book_id)
        else:
            raise RepositoryException("Book with given id does not exist!")

    def update_book(self, book_id, title, author):
        """
            This function updates the title and author of a book in the book repository.
            - it verifies if the inputs for book id, title and author are correct
            - it verifies if the book exists in the repository
        :param book_id: given book id
        :param title: given new title
        :param author: given new name of author
        """
        if not book_id.isnumeric():
            raise IdException("Invalid input for the ID!")
        updated_book = Book(int(book_id), title, author)
        self._book_validator.validate_book(updated_book)
        does_book_exist, book = self.find_book(book_id)
        if does_book_exist:
            self._undo_redo_service.add_undo_redo_operations(UndoRedoObject(lambda: self.book_repository.update_book(book),
                                                                            lambda: self.book_repository.update_book(updated_book)))
            self._book_repository.update_book(updated_book)
        else:
            raise RepositoryException("Update failed! This book id does not exist in the repository!")

    def search_book_by_id(self, given_id):
        book_matches_list = []
        books_list = self.data_from_books_repository()
        for book in books_list:
            if re.search(given_id, str(book.book_id), re.IGNORECASE):
                book_matches_list.append(book)
        return book_matches_list

    def search_book_by_title(self, given_title):
        book_matches_list = []
        books_list = self.data_from_books_repository()
        for book in books_list:
            if re.search(given_title, book.title, re.IGNORECASE):
                book_matches_list.append(book)
        return book_matches_list

    def search_book_by_author(self, given_author):
        book_matches_list = []
        books_list = self.data_from_books_repository()
        for book in books_list:
            if re.search(given_author, book.author, re.IGNORECASE):
                book_matches_list.append(book)
        return book_matches_list

    # -------------- CLIENT SERVICE FUNCTIONS --------------
    def data_from_clients_repository(self):
        """
            This function returns a list of all clients from the client repository.
        :return: the list of clients
        """
        clients_list = self._client_repository.clients_data_list()
        return clients_list

    def add_client(self, client_id, name):
        """
            This function adds a client to the client repository.
            - it verifies if the inputs for client id and name are correct
            - it verifies if the input for the client id does not already exist in the client repository
        :param client_id: given id
        :param name: given name
        """
        if not client_id.isnumeric():
            raise IdException("Invalid input for the ID!")
        client = Client(int(client_id), name)
        self._client_validator.validate_client(client)
        does_client_exist, client1 = self.find_client(client_id)
        if does_client_exist:
            raise RepositoryException("This client id already exists! ")
        self._undo_redo_service.add_undo_redo_operations(UndoRedoObject(lambda: self.client_repository.remove_client(client_id),
                                                                        lambda: self.client_repository.add_client(client)))
        self._client_repository.add_client(client)

    def remove_client(self, client_id):
        """
            This functions deletes the client with the given id from the client repository.
            - it verifies if the input for client id is correct
            - it verifies if the client exists in the repository
            - it verifies if the client is rented, and it deletes its rental if it's rented
        :param client_id: given id
        """
        if not client_id.isnumeric():
            raise IdException("Invalid input for the ID!")
        does_client_exist, client = self.find_client(client_id)
        if does_client_exist:
            client_has_rental, rental_ids_list = self.client_has_rentals(int(client_id))
            if client_has_rental:
                list_of_client_rentals = self.create_rentals_list_for_a_given_client(client_id)

            def undo_function():
                if client_has_rental:
                    if len(list_of_client_rentals) != 0:
                        for rental in list_of_client_rentals:
                            self.rental_repository.add_rental(rental)
                self.client_repository.add_client(client)

            def redo_function():
                if client_has_rental:
                    for a_rental_id in rental_ids_list:
                        self.rental_repository.delete_rental(int(a_rental_id))
                self.client_repository.remove_client(client_id)

            self._undo_redo_service.add_undo_redo_operations(UndoRedoObject(undo_function, redo_function))
            if client_has_rental:
                for a_rental_id in rental_ids_list:
                    self.rental_repository.delete_rental(int(a_rental_id))
            self._client_repository.remove_client(client_id)
        else:
            raise RepositoryException("Client with given id does not exist!")

    def update_client(self, client_id, name):
        """
            This function updates the name of a client in the client repository.
            - it verifies if the inputs for client id and name are correct
            - it verifies if the client exists in the repository
        :param client_id: given id
        :param name: given new name
        """
        if not client_id.isnumeric():
            raise IdException("Invalid input for the ID!")
        updated_client = Client(int(client_id), name)
        self._client_validator.validate_client(updated_client)
        does_client_exist, client = self.find_client(client_id)
        if does_client_exist:
            self._undo_redo_service.add_undo_redo_operations(UndoRedoObject(lambda: self.client_repository.update_client(client),
                                                                            lambda: self.client_repository.update_client(updated_client)))
            self._client_repository.update_client(updated_client)
        else:
            raise RepositoryException("Update failed! This client id does not exist in the repository!")

    def search_client_by_name(self, given_name):
        client_matches_list = []
        clients_list = self.data_from_clients_repository()
        for client in clients_list:
            if re.search(given_name, client.name, re.IGNORECASE):
                client_matches_list.append(client)
        return client_matches_list

    def search_client_by_id(self, given_id):
        client_matches_list = []
        clients_list = self.data_from_clients_repository()
        for client in clients_list:
            if re.search(given_id, str(client.client_id), re.IGNORECASE):
                client_matches_list.append(client)
        return client_matches_list

    # -------------- RENTAL SERVICE FUNCTIONS --------------
    def data_from_rentals_repository(self):
        """
            This function returns a list of all rentals from the rental repository.
        :return: the list of rentals
        """
        rentals_list = self._rental_repository.rentals_data_list()
        return rentals_list

    def rent_book(self, rental_id, book_id, client_id, rented_date):
        """
            This function creates a rental for a book.
            - it verifies if the inputs for rental id, book id, client id and rental date are correct
            - it verifies if the rental id does not already exist in the rental repository
            - it verifies if the book is not already rented
        :param rental_id: given rental id
        :param book_id: given book id
        :param client_id: given client id
        :param rented_date: given rental date
        """
        if not rental_id.isnumeric():
            raise IdException("Invalid input for the rental ID!")
        if not book_id.isnumeric():
            raise IdException("Invalid input for the book ID!")
        if not client_id.isnumeric():
            raise IdException("Invalid input for the client ID!")
        does_rental_exist, rental_date, rental = self.find_rental(rental_id)
        if does_rental_exist:
            raise RepositoryException("There already exists a rental with the same ID!")
        is_book_rented, rent_id = self.is_book_rented(int(book_id))
        if is_book_rented:
            raise RentalException("This book is already rented!")
        does_book_exist, book = self.find_book(book_id)
        if not does_book_exist:
            raise RentalException("This book does not exist!")
        does_client_exist, client = self.find_client(client_id)
        if not does_client_exist:
            raise RentalException("This client does not exist!")
        self._rental_validator.is_rental_date_valid(rented_date)
        day, month, year = rented_date.split('/')
        rented_date = datetime.date(int(year.strip()), int(month.strip()), int(day.strip()))
        book_rental = Rental(int(rental_id), int(book_id), int(client_id), rented_date)

        self._undo_redo_service.add_undo_redo_operations(UndoRedoObject(lambda: self.rental_repository.delete_rental(int(rental_id)),
                                                                        lambda: self.rental_repository.add_rental(book_rental)))
        self._rental_repository.add_rental(book_rental)

    def return_book(self, rental_id, return_date):
        """
            This function deletes the rental for a book.
            - it verifies if the inputs for rental id and return date are correct
            - it verifies if the rental id exists in the rental repository
        :param rental_id:
        :param return_date:
        """
        if not rental_id.isnumeric():
            raise IdException("Invalid input for the rental ID!")
        does_rental_exist, rental_date, rental = self.find_rental(int(rental_id))
        if does_rental_exist:
            self._rental_validator.is_return_date_valid(return_date, rental_date)
            day, month, year = return_date.split('/')
            return_date = datetime.date(int(year.strip()), int(month.strip()), int(day.strip()))

            def undo_function():
                self.rental_repository.rentals_data_list()[rental.rental_id - 1].returned_date = None

            self._undo_redo_service.add_undo_redo_operations(UndoRedoObject(undo_function,
                                                                            lambda: self.rental_repository.return_book(int(rental_id), return_date)))
            self._rental_repository.return_book(int(rental_id), return_date)
        else:
            raise RentalException("There does not exist any rental with this ID")

    # -------------- STATISTICS SERVICE FUNCTIONS --------------
    def create_statistics_for_most_rented_books(self):
        """
            This function creates a dictionary where the keys are the book ids and the values are the number of times
        that book was rented.
        :return: the most rented books dictionary
        """
        rentals_data_list = self.data_from_rentals_repository()
        books_data_list = self.data_from_books_repository()
        most_rented_books = {}
        for book in books_data_list:
            current_book_id = book.book_id
            most_rented_books[current_book_id] = 0
        for rental in rentals_data_list:
            current_rental_book_id = rental.book_id
            most_rented_books[current_rental_book_id] += 1
        return most_rented_books

    def create_and_sort_list_of_statistics_for_most_rented_books(self, most_rented_books_dictionary):
        """
            This function creates a list of books with number of times they were rented from a given dictionary
        containing as keys the book ids and as values the number of times those books were rented. It also sorts the list
        descending by the number of times the books were rented.
        :param most_rented_books_dictionary: the given dictionary with the data
        :return: the sorted list of most rented books
        """
        books_data_list = self.data_from_books_repository()
        most_rented_books_list = []
        for book_id in most_rented_books_dictionary:
            current_book_number_of_rentals = most_rented_books_dictionary.get(book_id)
            for book in books_data_list:
                current_book_id = book.book_id
                if book_id == current_book_id:
                    most_rented_books_list.append(BooksWithRentals(book, current_book_number_of_rentals))
        most_rented_books_list.sort(key=lambda book_with_rentals: book_with_rentals.number_of_rentals, reverse=True)
        return most_rented_books_list

    def create_statistics_for_most_active_clients(self):
        """
            This function creates a dictionary where the keys are the client ids and the values are the number of book
        rental days the client has.
        :return: the most active clients dictionary
        """
        rentals_data_list = self.data_from_rentals_repository()
        clients_data_list = self.data_from_clients_repository()
        most_active_clients = {}
        for client in clients_data_list:
            current_client_id = client.client_id
            most_active_clients[current_client_id] = 0
        for rental in rentals_data_list:
            current_rental_client_id = rental.client_id
            length_of_rental = self._rental_repository.length_of_rental(rental.rental_id)
            most_active_clients[int(current_rental_client_id)] += length_of_rental
        return most_active_clients

    def create_and_sort_list_of_statistics_for_most_active_clients(self, most_active_clients_dictionary):
        """
            This function creates a list of clients with number of days of book rental from a given dictionary
        containing as keys the client ids and as values the number of days of book rentals. It also sorts the list
        descending by the number of days of book rentals.
        :param most_active_clients_dictionary: the given dictionary with the data
        :return: the sorted list of most active clients
        """
        clients_data_list = self.data_from_clients_repository()
        most_active_clients_list = []
        for client_id in most_active_clients_dictionary:
            current_client_number_of_book_rental_days = most_active_clients_dictionary.get(client_id)
            for client in clients_data_list:
                current_client_id = client.client_id
                if client_id == current_client_id:
                    most_active_clients_list.append(ClientsWithRentalDays(client, current_client_number_of_book_rental_days))
        most_active_clients_list.sort(key=lambda client_with_rental_days: client_with_rental_days.number_of_days_of_rentals, reverse=True)
        return most_active_clients_list

    def create_statistics_for_most_rented_authors(self):
        """
            This function creates a dictionary where the keys are the book authors and the values are the number of
        times books by that author were rented.
        :return: the most rented author dictionary
        """
        rentals_data_list = self.data_from_rentals_repository()
        books_data_list = self.data_from_books_repository()
        most_rented_author = {}
        for book in books_data_list:
            current_book_author = book.author
            if current_book_author not in most_rented_author:
                most_rented_author[current_book_author] = 0
        for rental in rentals_data_list:
            current_rental_book_id = rental.book_id
            for book in books_data_list:
                current_book_id = book.book_id
                current_book_author = book.author
                if current_book_id == current_rental_book_id:
                    most_rented_author[current_book_author] += 1
        return most_rented_author

    def create_and_sort_list_of_statistics_for_most_rented_authors(self, most_rented_author_dictionary):
        """
            This function creates a list of authors with number of times their books were rented from a given dictionary
        containing as keys the authors and as values the number of times their books were rented. It also sorts the list
        descending by the number of times books by those authors were rented.
        :param most_rented_author_dictionary: the given dictionary with the data
        :return: the sorted list of most rented authors
        """
        most_rented_author_list = []
        for author in most_rented_author_dictionary:
            current_author_number_of_rentals = most_rented_author_dictionary.get(author)
            most_rented_author_list.append(AuthorWithRentals(author, current_author_number_of_rentals))
        most_rented_author_list.sort(key=lambda author_with_rentals: author_with_rentals.number_of_rentals, reverse=True)
        return most_rented_author_list

    # -------------- UNDO/REDO SERVICE FUNCTIONS --------------
    def undo(self):
        self._undo_redo_service.undo()

    def redo(self):
        self._undo_redo_service.redo()
