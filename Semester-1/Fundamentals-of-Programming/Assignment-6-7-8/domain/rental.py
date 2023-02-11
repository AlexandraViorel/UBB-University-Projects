import datetime
import random


class Rental:
    def __init__(self, rental_id, book_id, client_id, rented_date, returned_date=None):
        self._rental_id = rental_id
        self._book_id = book_id
        self._client_id = client_id
        self._rented_date = rented_date
        self._returned_date = returned_date

    @property
    def rental_id(self):
        return self._rental_id

    @rental_id.setter
    def rental_id(self, rental_id):
        self._rental_id = rental_id

    @property
    def book_id(self):
        return self._book_id

    @book_id.setter
    def book_id(self, book_id):
        self._book_id = book_id

    @property
    def client_id(self):
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        self._client_id = client_id

    @property
    def rented_date(self):
        return self._rented_date

    @rented_date.setter
    def rented_date(self, rented_date):
        self._rented_date = rented_date

    @property
    def returned_date(self):
        return self._returned_date

    @returned_date.setter
    def returned_date(self, returned_date):
        self._returned_date = returned_date

    def __len__(self):
        if self._returned_date is not None:
            return (self._returned_date - self._rented_date).days + 1
        else:
            today = datetime.date.today()
            return (today - self._rented_date).days + 1

    def __str__(self):
        return "Rental ID: " + str(self.rental_id) + ", Book ID: " + str(self.book_id) + ", Client ID: " + \
               str(self.client_id) + ", Rented date: " + str(self.rented_date) + ", Returned date: " + \
               str(self.returned_date)


def is_leap_year(year):
    # This function verifies if the year given is a leap year or not.
    leap_year = 2020
    while year < leap_year:
        year = year + 4
    if year == leap_year:
        return True
    else:
        return False


def generate_random_rentals(n=10):
    books_list = list(range(2, 20))
    rentals_data = {}
    random_rental = Rental(1, 1, 1, datetime.date(2019, 12, 12))
    rentals_data[1] = random_rental
    for i in range(2, n+1):
        rental_id = i
        random_client_id = random.randint(1, 20)
        random_book_id = random.choice(books_list)
        books_list.remove(random_book_id)
        rented_date_year = random.randint(2019, 2020)
        rented_date_month = random.randint(1, 12)
        if rented_date_month == 2:
            if is_leap_year(rented_date_year):
                rented_date_day = random.randint(1, 29)
            else:
                rented_date_day = random.randint(1, 28)
        elif rented_date_month in [1, 3, 5, 7, 8, 10, 12]:
            rented_date_day = random.randint(1, 31)
        else:
            rented_date_day = random.randint(1, 30)
        random_rent_date = datetime.date(rented_date_year, rented_date_month, rented_date_day)
        random_generated_rental = Rental(rental_id, random_book_id, random_client_id, random_rent_date)
        rentals_data[rental_id] = random_generated_rental
    return rentals_data


class BooksWithRentals:
    def __init__(self, book, number_of_rentals):
        self._book = book
        self._number_of_rentals = number_of_rentals

    @property
    def book(self):
        return self._book

    @property
    def number_of_rentals(self):
        return self._number_of_rentals

    def __str__(self):
        return "Book: " + str(self.book.title) + " by " + str(self.book.author) + " was rented " + \
               str(self.number_of_rentals) + " times "


class ClientsWithRentalDays:
    def __init__(self, client, number_of_days_of_rentals):
        self._client = client
        self._number_of_days_of_rentals = number_of_days_of_rentals

    @property
    def client(self):
        return self._client

    @property
    def number_of_days_of_rentals(self):
        return self._number_of_days_of_rentals

    def __str__(self):
        return "Client: " + str(self.client.name) + " with id: " + str(self.client.client_id) + " has " + \
               str(self.number_of_days_of_rentals) + " days of book rentals"


class AuthorWithRentals:
    def __init__(self, author, number_of_rentals):
        self._author = author
        self._number_of_rentals = number_of_rentals

    @property
    def author(self):
        return self._author

    @property
    def number_of_rentals(self):
        return self._number_of_rentals

    def __str__(self):
        return "Books by " + str(self.author) + " were rented " + str(self.number_of_rentals) + " times"
