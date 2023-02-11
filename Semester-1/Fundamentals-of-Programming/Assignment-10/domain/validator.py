from src.domain.exceptions import BookValidatorExceptions
from src.domain.exceptions import ClientValidatorExceptions
from src.domain.exceptions import DateException
import datetime


class BookValidator:
    @staticmethod
    def is_title_valid(title):
        return not title.isnumeric() and not isinstance(title, float) and not isinstance(title, list) and \
               not isinstance(title, dict) and not isinstance(title, tuple) and not title.isspace()

    @staticmethod
    def is_author_valid(author):
        return not author.isnumeric() and not isinstance(author, float) and not isinstance(author, list) and \
               not isinstance(author, dict) and not isinstance(author, tuple) and not author.isspace()

    def validate_book(self, book):
        errors_list = []
        if not self.is_title_valid(book.title):
            errors_list.append("The title should be a string! ")
        if not self.is_author_valid(book.author):
            errors_list.append("The author should be a string! ")

        if len(errors_list) > 0:
            raise BookValidatorExceptions(errors_list)


class ClientValidator:
    @staticmethod
    def is_name_valid(name):
        return not name.isnumeric() and not isinstance(name, float) and not isinstance(name, list) and \
               not isinstance(name, dict) and not isinstance(name, tuple) and not name.isspace()

    def validate_client(self, client):
        errors_list = []
        if not self.is_name_valid(client.name):
            errors_list.append("The name should be a string! ")

        if len(errors_list) > 0:
            raise ClientValidatorExceptions(errors_list)


class RentalValidator:
    @staticmethod
    def is_rental_date_valid(rental_date):
        day, month, year = rental_date.split('/')
        try:
            datetime.date(int(year.strip()), int(month.strip()), int(day.strip()))
        except ValueError:
            raise DateException("Invalid rented date!")
        rental_date = datetime.date(int(year.strip()), int(month.strip()), int(day.strip()))
        if rental_date > datetime.date.today():
            raise DateException("Rental date cannot be after today!")

    @staticmethod
    def is_return_date_valid(return_date, rental_date):
        day, month, year = return_date.split('/')
        try:
            datetime.date(int(year.strip()), int(month.strip()), int(day.strip()))
        except ValueError:
            raise DateException("Invalid returned date!")
        return_date = datetime.date(int(year.strip()), int(month.strip()), int(day.strip()))
        if return_date < rental_date:
            raise DateException("Return date cannot be before rental date!")
