import datetime
from src.services.service import Service
from src.domain.exceptions import *
from src.domain.book import *
from src.domain.client import *
from src.domain.rental import Rental
from src.domain.rental import BooksWithRentals
from src.domain.rental import ClientsWithRentalDays
from src.domain.rental import AuthorWithRentals
from src.domain.rental import is_leap_year
from src.domain.rental import generate_random_rentals
from src.domain.validator import BookValidator
from src.domain.validator import ClientValidator
from src.domain.validator import RentalValidator
from src.repository.book_repository import BookRepository
from src.repository.rental_repository import RentalRepository
from src.repository.client_repository import ClientRepository
import unittest


class TestService(unittest.TestCase):
    def setUp(self) -> None:
        self._service = Service()

    # --- Test for data_from_clients_repository ---

    def test_dataFromClientsRepository__DoesNotHaveInput__ListOfClients(self):
        self.assertIsInstance(self._service.data_from_clients_repository(), list)

    # --- Tests for add_client ---

    def test_addClient__CorrectInput__ClientAddedToRepository(self):
        self._service.add_client("21", "Ale")
        self.assertEqual(len(self._service.client_repository), 21)

    def test_addClient__WrongInputForID__IdException(self):
        with self.assertRaises(IdException):
            self._service.add_client("a", "Ale")

    def test_addClient__WrongInputForName__ClientValidatorExceptions(self):
        with self.assertRaises(ClientValidatorExceptions):
            self._service.add_client("21", "1")

    def test_addClient__IdAlreadyInRepository__RepositoryException(self):
        with self.assertRaises(RepositoryException):
            self._service.add_client("1", "Ale")

    # --- Tests for remove_client ---

    def test_removeClient__CorrectInput__ClientRemovedFromRepository(self):
        self._service.remove_client("1")
        self.assertEqual(len(self._service.client_repository), 19)

    def test_removeClient__WrongInputForId__IdException(self):
        with self.assertRaises(IdException):
            self._service.remove_client("a")

    def test_removeClient__IdThatDoesNotExistInRepository__RepositoryException(self):
        with self.assertRaises(RepositoryException):
            self._service.remove_client("21")

    # --- Tests for update_client ---

    def test_updateClient__CorrectInput__ClientUpdatedInRepository(self):
        self._service.update_client("1", "Cristi")
        self.assertEqual(self._service.data_from_clients_repository()[0].name, "Cristi")

    def test_updateClient__WrongInputForId__IdException(self):
        with self.assertRaises(IdException):
            self._service.update_client("a", "Cristi")

    def test_updateClient__IdThatDoesNotExistInRepository__RepositoryException(self):
        with self.assertRaises(RepositoryException):
            self._service.update_client("21", "Cristi")

    def test_updateClient__WrongInputForNewName__ClientValidatorExceptions(self):
        with self.assertRaises(ClientValidatorExceptions):
            self._service.update_client("1", "1")

    # --- Test for data_from_books_repository ---

    def test_dataFromBooksRepository__DoesNotHaveInput__ListOfBooks(self):
        self.assertIsInstance(self._service.data_from_books_repository(), list)

    # --- Tests for add_book ---

    def test_addBook__CorrectInput__BookAddedToRepository(self):
        self._service.add_book("21", "Ugly love", "Colleen Hoover")
        self.assertEqual(len(self._service.book_repository), 21)

    def test_addBook__WrongInputForId__IdException(self):
        with self.assertRaises(IdException):
            self._service.add_book("a", "Ugly love", "Colleen Hoover")

    def test_addBook__IdAlreadyInRepository__RepositoryException(self):
        with self.assertRaises(RepositoryException):
            self._service.add_book("1", "Verity", "Colleen Hoover")

    def test_addBook__WrongInputForTitle__BookValidatorExceptions(self):
        with self.assertRaises(BookValidatorExceptions):
            self._service.add_book("21", "1", "Colleen Hoover")

    def test_addBook__WrongInputForAuthor__BookValidatorExceptions(self):
        with self.assertRaises(BookValidatorExceptions):
            self._service.add_book("1", "Ugly love", "1")

    # --- Tests for remove_book ---

    def test_removeBook__CorrectInput__BookRemovedFromRepository(self):
        self._service.remove_book("1")
        self.assertEqual(len(self._service.book_repository), 19)

    def test_removeBook__WrongInputForId__IdException(self):
        with self.assertRaises(IdException):
            self._service.remove_book("a")

    def test_removeBook__IdThatDoesNotExistInRepository__RepositoryException(self):
        with self.assertRaises(RepositoryException):
            self._service.remove_book("21")

    # --- Tests for update_book ---

    def test_updateBook__CorrectInput__BookUpdatedInRepository(self):
        self._service.update_book("1", "Ion", "Liviu Rebreanu")
        self.assertEqual(self._service.data_from_books_repository()[0].title, "Ion")
        self.assertEqual(self._service.data_from_books_repository()[0].author, "Liviu Rebreanu")

    def test_updateBook__WrongInputForId__IdException(self):
        with self.assertRaises(IdException):
            self._service.update_book("a", "Ion", "Liviu Rebreanu")

    def test_updateBook__IdThatDoesNotExistInRepository__RepositoryException(self):
        with self.assertRaises(RepositoryException):
            self._service.update_book("21", "Ugly love", "Colleen Hoover")

    def test_updateBook__WrongInputForNewTitle__BookValidatorExceptions(self):
        with self.assertRaises(BookValidatorExceptions):
            self._service.update_book("1", "1", "Liviu Rebreanu")

    def test_updateBook__WrongInputForAuthor__BookValidatorExceptions(self):
        with self.assertRaises(BookValidatorExceptions):
            self._service.update_book("1", "Ion", "1")

    # --- Test for data_from_rentals_repository ---

    def test_dataFromRentalsRepository__DoesNotHaveInput__ListOfRentals(self):
        self.assertIsInstance(self._service.data_from_rentals_repository(), list)

    # --- Tests for rent_book ---

    def test_rentBook__CorrectInput__RentalAddedToRentalsRepository(self):
        self._service.rent_book("11", "20", "1", "20/11/2020")
        self.assertEqual(len(self._service.rental_repository), 11)

    def test_rentBook__WrongInputForRentalId__IdException(self):
        with self.assertRaises(IdException):
            self._service.rent_book("a", "20", "1", "20/11/2020")

    def test_rentBook__WrongInputForBookId__IdException(self):
        with self.assertRaises(IdException):
            self._service.rent_book("11", "a", "1", "20/11/2020")

    def test_rentBook__WrongInputForClientId__IdException(self):
        with self.assertRaises(IdException):
            self._service.rent_book("11", "20", "a", "20/11/2020")

    def test_rentBook__WrongInputForRentedDate__DateException(self):
        with self.assertRaises(DateException):
            self._service.rent_book("11", "20", "1", "200/10/2020")

    def test_rentBook__RentedDateAfterToday__DateException(self):
        with self.assertRaises(DateException):
            self._service.rent_book("11", "20", "1", "12/12/2022")

    def test_rentBook__RentalIdAlreadyInRepository__RepositoryException(self):
        with self.assertRaises(RepositoryException):
            self._service.rent_book("1", "20", "2", "20/11/2020")

    def test_rentBook__BookIdDoesNotExist__RentalException(self):
        with self.assertRaises(RentalException):
            self._service.rent_book("11", "100", "1", "20/11/2020")

    def test_rentBook__ClientIdDoesNotExist__RentalException(self):
        with self.assertRaises(RentalException):
            self._service.rent_book("11", "20", "100", "20/11/2020")

    def test_rentBook__BookAlreadyRented__RentalException(self):
        with self.assertRaises(RentalException):
            self._service.rent_book("11", "1", "5", "20/11/2020")

    # --- Tests for return_book ---

    def test_returnBook__CorrectInput__RentalReturnedDateModified(self):
        self._service.return_book("1", "21/11/2021")
        self.assertEqual(self._service.data_from_rentals_repository()[0].returned_date, datetime.date(2021, 11, 21))

    def test_returnBook__WrongInputForRentalId__IdException(self):
        with self.assertRaises(IdException):
            self._service.return_book("a", "21/11/2021")

    def test_returnBook__WrongInputForReturnDate__DateException(self):
        with self.assertRaises(DateException):
            self._service.return_book("1", "200/11/2021")

    def test_returnBook__ReturnDateBeforeRentalDate__DateException(self):
        with self.assertRaises(DateException):
            self._service.return_book("1", "10/10/2000")

    def test_returnBook__RentalIdDoesNotExistInRepository__RentalException(self):
        with self.assertRaises(RentalException):
            self._service.return_book("11", "21/11/2021")

    # --- Tests for search_book_by_id ---

    def test_searchBookById__CorrectInput__ListOfSearchResults(self):
        self.assertEqual(len(self._service.search_book_by_id("1")), 11)

    def test_searchBookById__InputThatReturnsNoMatches__EmptyList(self):
        self.assertEqual(len(self._service.search_book_by_id("a")), 0)

    # --- Tests for search_book_by_title ---

    def test_searchBookByTitle__CorrectInput__ListOfSearchResults(self):
        self.assertEqual(len(self._service.search_book_by_title("Ugly")), 1)

    def test_searchBookByTitle__InputThatReturnsNoMatches__EmptyList(self):
        self.assertEqual(len(self._service.search_book_by_title("abcdef")), 0)

    # --- Tests for search_book_by_author ---

    def test_searchBookByAuthor__CorrectInput__ListOfSearchResults(self):
        self.assertEqual(len(self._service.search_book_by_author("Irina")), 3)

    def test_searchBookByAuthor__InputThatReturnsNoMatches__EmptyList(self):
        self.assertEqual(len(self._service.search_book_by_author("abcdef")), 0)

    # --- Tests for search_client_by_id ---

    def test_searchClientById__CorrectInput__ListOfSearchResults(self):
        self.assertEqual(len(self._service.search_client_by_id("1")), 11)

    def test_searchClientById__InputThatReturnsNoMatches__EmptyList(self):
        self.assertEqual(len(self._service.search_client_by_id("abcdef")), 0)

    # --- Tests for search_client_by_name ---

    def test_searchClientByName__CorrectInput__ListOfSearchResults(self):
        self.assertNotEqual(len(self._service.search_client_by_name("Alexandra")), 0)

    def test_searchClientByName__InputThatReturnsNoMatches__EmptyList(self):
        self.assertEqual(len(self._service.search_client_by_name("abcdef")), 0)

    # --- Test for create_statistics_for_most_rented_books ---
    def test_createStatisticsForMostRentedBooks__NoInput__DictionaryOfMostRentedBooks(self):
        self.assertIsInstance(self._service.create_statistics_for_most_rented_books(), dict)

    # --- Test for create_and_sort_list_of_statistics_for_most_rented_books ---
    def test_createAndSortListOfStatisticsForMostRentedBooks__CorrectInput__SortedListOfMostRentedBooks(self):
        most_rented_books_dictionary = self._service.create_statistics_for_most_rented_books()
        self.assertIsInstance(self._service.create_and_sort_list_of_statistics_for_most_rented_books(most_rented_books_dictionary),
                              list)

    # --- Test for create_statistics_for_most_active_clients ---
    def test_createStatisticsForMostActiveClients__NoInput__DictionaryOfMostActiveClients(self):
        self.assertIsInstance(self._service.create_statistics_for_most_active_clients(), dict)

    # --- Test for create_and_sort_list_of_statistics_for_most_active_clients ---
    def test_createAndSortListOfStatisticsForMostActiveClients__CorrectInput__SortedListOfMostActiveClients(self):
        most_active_clients_dictionary = self._service.create_statistics_for_most_active_clients()
        self.assertIsInstance(self._service.create_and_sort_list_of_statistics_for_most_active_clients(most_active_clients_dictionary),
                              list)

    # --- Test for create_statistics_for_most_rented_authors ---
    def test_createStatisticsForMostRentedAuthors__NoInput__DictionaryOfMostRentedAuthors(self):
        self.assertIsInstance(self._service.create_statistics_for_most_rented_authors(), dict)

    # --- Test for create_and_sort_list_of_statistics_for_most_rented_authors ---
    def test_createAndSortListOfStatisticsForMostRentedAuthors__CorrectInput__SortedListOfMostRentedAuthors(self):
        most_rented_authors_dictionary = self._service.create_statistics_for_most_rented_authors()
        self.assertIsInstance(self._service.create_and_sort_list_of_statistics_for_most_rented_authors(most_rented_authors_dictionary),
                              list)

    # --- Tests for undo/redo ---
    def test_undoNoOperation__NoInput__UndoRedoException(self):
        with self.assertRaises(UndoRedoException):
            self._service.undo()

    def test_redoNoOperation__NoInput__UndoRedoException(self):
        with self.assertRaises(UndoRedoException):
            self._service.redo()

    def test_undoRedoAnAddBook__NoInput__OperationUndoneAndRedone(self):
        self._service.add_book("21", "House of Gucci", "Sara Gay Forden")
        self._service.undo()
        self.assertEqual(len(self._service.book_repository), 20)
        self._service.redo()
        self.assertEqual(len(self._service.book_repository), 21)

    def test_undoRedoARemoveBook__NoInput__OperationUndoneAndRedone(self):
        self._service.remove_book("1")
        self._service.undo()
        self.assertEqual(len(self._service.book_repository), 20)
        self._service.redo()
        self.assertEqual(len(self._service.book_repository), 19)

    def test_undoRedoAnUpdateBook__NoInput__OperationUndoneAndRedone(self):
        self._service.update_book("1", "House of Gucci", "Sara Gay Forden")
        self._service.undo()
        self.assertEqual(self._service.data_from_books_repository()[0].title, "Ugly love")
        self._service.redo()
        self.assertEqual(self._service.data_from_books_repository()[0].title, "House of Gucci")

    def test_undoRedoAnAddClient__NoInput__OperationUndoneAndRedone(self):
        self._service.add_client("21", "Ale")
        self._service.undo()
        self.assertEqual(len(self._service.client_repository), 20)
        self._service.redo()
        self.assertEqual(len(self._service.client_repository), 21)

    def test_undoRedoARemoveClient__NoInput__OperationUndoneAndRedone(self):
        self._service.remove_client("1")
        self._service.undo()
        self.assertEqual(len(self._service.client_repository), 20)
        self._service.redo()
        self.assertEqual(len(self._service.client_repository), 19)

    def test_undoRedoAnUpdateClient__NoInput__OperationUndoneAndRedone(self):
        self._service.update_client("1", "Andrei")
        self._service.undo()
        self.assertEqual(self._service.data_from_clients_repository()[0].name, "Alexandra")
        self._service.redo()
        self.assertEqual(self._service.data_from_clients_repository()[0].name, "Andrei")

    def test_undoRedoAReturnBook__NoInput__OperationUndoneAndRedone(self):
        self._service.return_book("10", "12/10/2021")
        self._service.undo()
        self.assertEqual(self._service.data_from_rentals_repository()[9].returned_date, None)
        self._service.redo()
        self.assertEqual(self._service.data_from_rentals_repository()[9].returned_date, datetime.date(2021, 10, 12))

    def test_wasBookRented__BookIdThatWasNotRented__FalseAndNone(self):
        self.assertEqual(self._service.was_book_rented("20"), (False, None))

    def test_clientHasRentals__ClientIdThatHasNoRentals__FalseAndNone(self):
        self.assertEqual(self._service.client_has_rentals("100000"), (False, None))

    def test_correctStack__NoInput__StackCorrected(self):
        self._service.add_client("21", "ale")
        self._service.add_client("22", "andrei")
        self._service.undo()
        self._service.undo()
        self._service.redo()
        self._service.add_client("23", "ale")
        self.assertEqual(len(self._service._undo_redo_service.undo_stack), 2)

    def tearDown(self) -> None:
        pass


class TestBookDomain(unittest.TestCase):
    def setUp(self) -> None:
        self._correct_book_id = 1
        self._correct_book_title = "House of Gucci"
        self._correct_book_author = "Sara Gay Forden"
        self._book = Book(self._correct_book_id, self._correct_book_title, self._correct_book_author)

    def test_BookIdGetter(self):
        self.assertEqual(self._book.book_id, self._correct_book_id)

    def test_TitleGetter(self):
        self.assertEqual(self._book.title, self._correct_book_title)

    def test_AuthorGetter(self):
        self.assertEqual(self._book.author, self._correct_book_author)

    def test_bookIdSetter(self):
        self._book.book_id = 2
        self.assertEqual(self._book.book_id, 2)

    def test_titleSetter(self):
        self._book.title = "Ugly love"
        self.assertEqual(self._book.title, "Ugly love")

    def test_authorSetter(self):
        self._book.author = "Colleen Hoover"
        self.assertEqual(self._book.author, "Colleen Hoover")

    def test_bookString__NoInput__String(self):
        self.assertEqual(str(self._book), "Book id: 1, House of Gucci by Sara Gay Forden")

    def test_generateRandomBook__NoOfBooks__RandomGeneratedBooksDictionary(self):
        self.assertIsInstance(generate_random_books(), dict)
        self.assertEqual(len(generate_random_books()), 20)

    def tearDown(self) -> None:
        pass


class TestClientDomain(unittest.TestCase):
    def setUp(self) -> None:
        self._correct_client_id = 1
        self._correct_name = "Alexandra"
        self._client = Client(self._correct_client_id, self._correct_name)

    def test_clientIdGetter__NoInput__ClientId(self):
        self.assertEqual(self._client.client_id, self._correct_client_id)

    def test_clientNameGetter__NoInput__Name(self):
        self.assertEqual(self._client.name, self._correct_name)

    def test_clientIdSetter__NoInput__ChangedId(self):
        self._client.client_id = 2
        self.assertEqual(self._client.client_id, 2)

    def test_clientNameSetter__NoInput__ChangedName(self):
        self._client.name = "Andrei"
        self.assertEqual(self._client.name, "Andrei")

    def test_clientString__NoInput__String(self):
        self.assertEqual(str(self._client), "Client id: 1, Name: Alexandra")

    def tearDown(self) -> None:
        pass


class TestRentalDomain(unittest.TestCase):
    def setUp(self) -> None:
        self._rental = Rental(1, 1, 1, datetime.date(2020, 12, 12), datetime.date(2020, 12, 15))
        self._rental_with_no_return_date = Rental(2, 2, 2, datetime.date(2021, 12, 1))
        self._book = Book(1, "House of Gucci", "Sara Gay Forden")
        self._number_of_rentals_for_book = 3
        self._book_with_rentals = BooksWithRentals(self._book, self._number_of_rentals_for_book)
        self._client = Client(1, "Alexandra")
        self._number_of_days_of_rentals = 10
        self._client_with_rental_days = ClientsWithRentalDays(self._client, self._number_of_days_of_rentals)
        self._author = "Sara Gay Forden"
        self._number_of_rentals_for_author = 3
        self._author_with_rentals = AuthorWithRentals(self._author, self._number_of_rentals_for_author)

    def test_rentalIdSetter__NoInput__ChangedRentalId(self):
        self._rental.rental_id = 2
        self.assertEqual(self._rental.rental_id, 2)

    def test_bookIdSetter__NoInput__ChangedBookId(self):
        self._rental.book_id = 2
        self.assertEqual(self._rental.book_id, 2)

    def test_clientIdSetter__NoInput__ChangedClientId(self):
        self._rental.client_id = 2
        self.assertEqual(self._rental.client_id, 2)

    def test_rentedDateSetter__NoInput__ChangedRentedDate(self):
        self._rental.rented_date = datetime.date(2021, 11, 22)
        self.assertEqual(self._rental.rented_date, datetime.date(2021, 11, 22))

    def test_returnedDateSetter__NoInput__ChangedReturnedDate(self):
        self._rental.returned_date = datetime.date(2021, 12, 1)
        self.assertEqual(self._rental.returned_date, datetime.date(2021, 12, 1))

    def test_rentalString__Rental__String(self):
        self.assertEqual(str(self._rental), "Rental ID: 1, Book ID: 1, Client ID: 1, Rented date: 2020-12-12, "
                                            "Returned date: 2020-12-15")

    def test_rentalLength__Rental__LengthOfRental(self):
        self.assertEqual(len(self._rental), 4)

    def test_rentalLength__RentalWithoutReturnDate__LengthOfRental(self):
        self.assertEqual(len(self._rental_with_no_return_date), 3)

    def test_bookGetter__NoInout__Book(self):
        self.assertEqual(self._book_with_rentals.book, self._book)

    def test_numberOfRentalsForBookGetter__NoInput__NumberOfRentals(self):
        self.assertEqual(self._book_with_rentals.number_of_rentals, self._number_of_rentals_for_book)

    def test_booksWithRentalsString__BookWithRental__String(self):
        self.assertEqual(str(self._book_with_rentals), "Book: House of Gucci by Sara Gay Forden was rented 3 times ")

    def test_clientGetter__NoInput__Client(self):
        self.assertEqual(self._client_with_rental_days.client, self._client)

    def test_numberOfRentalDaysGetter__NoInput__NumberOfRentalDays(self):
        self.assertEqual(self._client_with_rental_days.number_of_days_of_rentals, self._number_of_days_of_rentals)

    def test_clientWithRentalDaysString__ClientWithRentalDays__String(self):
        self.assertEqual(str(self._client_with_rental_days), "Client: Alexandra with id: 1 has 10 days of book rentals")

    def test_authorGetter__NoInput__Author(self):
        self.assertEqual(self._author_with_rentals.author, self._author)

    def test_numberOfRentalsForAuthorGetter__NoInput__NumberOfRentals(self):
        self.assertEqual(self._author_with_rentals.number_of_rentals, self._number_of_rentals_for_author)

    def test_authorWithRentalsString__AuthorWithRentals__String(self):
        self.assertEqual(str(self._author_with_rentals), "Books by Sara Gay Forden were rented 3 times")

    def test_isLeapYear__ALeapYear__True(self):
        self.assertTrue(is_leap_year(2020))

    def test_isLeapYear__NotALeapYear__False(self):
        self.assertFalse(is_leap_year(2019))

    def test_generateRandomRentals__NumberOfRentals__RentalsDictionary(self):
        self.assertIsInstance(generate_random_rentals(), dict)

    def tearDown(self) -> None:
        pass


class TestBookRepository(unittest.TestCase):
    def setUp(self) -> None:
        self._book_repository = BookRepository()

    def test_booksDataList__NoInput__List(self):
        self.assertIsInstance(self._book_repository.books_data_list(), list)

    def test_setItem__KeyAndValue__ItemAddedToBooksData(self):
        self._book_repository.__setitem__("21", Book(21, "ABC", "ABC"))
        self.assertEqual(len(self._book_repository), 21)

    def test_delItem__key__ItemDeletedFromBooksData(self):
        self._book_repository.__delitem__(1)
        self.assertEqual(len(self._book_repository), 19)

    def test_addBook__givenBook__BookAddedToBooksData(self):
        self._book_repository.add_book(Book(21, "ABC", "ABC"))
        self.assertEqual(len(self._book_repository), 21)

    def test_removeBook__bookId__BookRemovedFromBooksData(self):
        self._book_repository.remove_book("1")
        self.assertEqual(len(self._book_repository), 19)

    def test_updateBook__UpdatedBook__BookUpdatedInBooksData(self):
        self._book_repository.update_book(Book(1, "abc", "abc"))
        self.assertEqual(self._book_repository.books_data_list()[0].title, "abc")

    def tearDown(self) -> None:
        pass


class TestClientRepository(unittest.TestCase):
    def setUp(self) -> None:
        self._client_repository = ClientRepository()

    def test_clientsDataList__NoInput__List(self):
        self.assertIsInstance(self._client_repository.clients_data_list(), list)

    def test_setItem__KeyAndValue__ItemAddedToClientsData(self):
        self._client_repository.__setitem__("21", Client(21, "ABC"))
        self.assertEqual(len(self._client_repository), 21)

    def test_delItem__key__ItemDeletedFromClientsData(self):
        self._client_repository.__delitem__(1)
        self.assertEqual(len(self._client_repository), 19)

    def test_addClient__givenClient__ClientAddedToClientsData(self):
        self._client_repository.add_client(Client(21, "ABC"))
        self.assertEqual(len(self._client_repository), 21)

    def test_removeClient__clientId__ClientRemovedFromClientsData(self):
        self._client_repository.remove_client("1")
        self.assertEqual(len(self._client_repository), 19)

    def test_updateClient__UpdatedClient__ClientUpdatedInClientsData(self):
        self._client_repository.update_client(Client(1, "abc"))
        self.assertEqual(self._client_repository.clients_data_list()[0].name, "abc")

    def tearDown(self) -> None:
        pass


class TestRentalRepository(unittest.TestCase):
    def setUp(self) -> None:
        self._rental_repository = RentalRepository()

    def test_rentalsDataList__NoInput__List(self):
        self.assertIsInstance(self._rental_repository.rentals_data_list(), list)

    def test_setItem__KeyAndValue__ItemAddedToRentalsData(self):
        self._rental_repository.__setitem__("21", Rental(21, 20, 1, datetime.date(2020, 11, 11)))
        self.assertEqual(len(self._rental_repository), 11)

    def test_lengthOfRental__RentalId__LengthOfRental(self):
        self._rental_repository.add_rental(Rental(21, 20, 1, datetime.date(2021, 12, 1), datetime.date(2021, 12, 3)))
        self.assertEqual(self._rental_repository.length_of_rental(21), 3)

    def test_lengthOfRental__RentalIdWithNoReturnDate__LengthOfRental(self):
        self._rental_repository.add_rental(Rental(21, 20, 1, datetime.date(2021, 12, 1)))
        self.assertEqual(self._rental_repository.length_of_rental(21), 3)

    def test_delItem__key__ItemDeletedFromRentalsData(self):
        self._rental_repository.__delitem__(1)
        self.assertEqual(len(self._rental_repository), 9)

    def test_addRental__givenRental__RentalAddedToRentalsData(self):
        self._rental_repository.add_rental(Rental(21, 20, 1, datetime.date(2020, 11, 11)))
        self.assertEqual(len(self._rental_repository), 11)

    def test_deleteRental__RentalId__RentalRemovedFromRentalsData(self):
        self._rental_repository.delete_rental(1)
        self.assertEqual(len(self._rental_repository), 9)

    def test_returnBook__RentalIdAndReturnDate__RentalUpdatedInRentalsData(self):
        self._rental_repository.return_book("1", datetime.date(2021, 12, 1))
        self.assertEqual(self._rental_repository.rentals_data_list()[0].returned_date, datetime.date(2021, 12, 1))

    def tearDown(self) -> None:
        pass


class TestExceptions(unittest.TestCase):
    def setUp(self) -> None:
        self._IdException = IdException
        self._UndoRedoException = UndoRedoException
        self._DateException = DateException
        self._RepositoryException = RepositoryException
        self._RentalException = RentalException
        self._BookException = BookException
        self._BookValidatorExceptions = BookValidatorExceptions
        self._ClientException = ClientException
        self._ClientValidatorExceptions = ClientValidatorExceptions

    def test_IdExceptionString__message__string(self):
        self.assertEqual(str(IdException("Invalid Id")), "Invalid Id")

    def test_UndoRedoExceptionString__message__string(self):
        self.assertEqual(str(UndoRedoException("No operations to undo")), "No operations to undo")

    def test_DateExceptionString__message__string(self):
        self.assertEqual(str(DateException("Invalid date")), "Invalid date")

    def test_RepositoryExceptionString__message__string(self):
        self.assertEqual(str(RepositoryException("Client already in repository!")), "Client already in repository!")

    def test_RentalExceptionString__message__string(self):
        self.assertEqual(str(RentalException("Book already rented")), "Book already rented")

    def test_BookExceptionString__message__string(self):
        self.assertEqual(str(BookException("Invalid title")), "Invalid title")

    def test_BookValidatorExceptionsString__messageList__string(self):
        self.assertEqual(str(BookValidatorExceptions(["Invalid title", "Invalid id"])), "Invalid title\nInvalid id\n")

    def test_ClientExceptionString__message__string(self):
        self.assertEqual(str(ClientException("Invalid name")), "Invalid name")

    def test_ClientValidatorExceptions__messageList__string(self):
        self.assertEqual(str(ClientValidatorExceptions(["Invalid name", "Invalid id"])), "Invalid name\nInvalid id\n")

    def tearDown(self) -> None:
        pass


class TestValidator(unittest.TestCase):
    def setUp(self) -> None:
        self._book_validator = BookValidator()
        self._wrong_book_id = "a"
        self._wrong_book_title = "1"
        self._wrong_book_author = "1"
        self._wrong_book = Book(self._wrong_book_id, self._wrong_book_title, self._wrong_book_author)
        self._rental_validator = RentalValidator()
        self._client_validator = ClientValidator()
        self._wrong_client_id = "a"
        self._wrong_name = "1"
        self._wrong_client = Client(self._wrong_client_id, self._wrong_name)

    def test_bookValidator_BookWithWrongIdTitleAndAuthor__BookValidatorException(self):
        with self.assertRaises(BookValidatorExceptions):
            self._book_validator.validate_book(self._wrong_book)

    def test_clientValidator__ClientWithWrongIdAndName__ClientValidatorException(self):
        with self.assertRaises(ClientValidatorExceptions):
            self._client_validator.validate_client(self._wrong_client)

    def test_rentalValidator__InvalidRentalDate__DateException(self):
        with self.assertRaises(DateException):
            self._rental_validator.is_rental_date_valid("120/10/2020")

    def test_rentalValidator__RentalDateAfterToday__DateException(self):
        with self.assertRaises(DateException):
            self._rental_validator.is_rental_date_valid("12/12/2023")

    def test_rentalValidator__InvalidReturnDate__DateException(self):
        with self.assertRaises(DateException):
            self._rental_validator.is_return_date_valid("120/12/2020", "12/11/2020")

    def test_rentalValidator__ReturnDateBeforeRentalDate__DateException(self):
        with self.assertRaises(DateException):
            self._rental_validator.is_return_date_valid("10/12/2020", datetime.date(2020, 12, 12))

    def tearDown(self) -> None:
        pass
