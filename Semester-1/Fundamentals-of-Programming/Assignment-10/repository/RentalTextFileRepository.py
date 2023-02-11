from src.domain.rental import Rental
from src.repository.RentalRepository import RentalRepository
from src.domain.exceptions import FileException
import datetime


class RentalTextFileRepository(RentalRepository):
    def __init__(self, file_name):
        RentalRepository.__init__(self)
        self._file_name = file_name
        self._load_file()

    def _load_file(self):
        try:
            file = open(self._file_name, "r")
        except IOError:
            raise FileException("Error! File not found!")
        line = file.readline().strip()
        while line != "":
            values = line.split(";")
            rented_year, rented_month, rented_day = values[3].split("-")
            rented_date = datetime.date(int(rented_year), int(rented_month), int(rented_day))
            if values[4] != "None":
                return_year, return_month, return_day = values[4].split("-")
                return_date = datetime.date(int(return_year), int(return_month), int(return_day))
            else:
                return_date = None
            rental = Rental(int(values[0]), int(values[1]), int(values[2]), rented_date, return_date)
            RentalRepository.add_rental(self, rental)
            line = file.readline().strip()
        file.close()

    @staticmethod
    def _rental_string(rental):
        return str(rental.rental_id) + ";" + str(rental.book_id) + ";" + str(rental.client_id) + ";" + \
               str(rental.rented_date) + ";" + str(rental.returned_date)

    def _save_file(self):
        file = open(self._file_name, "w")
        rentals_list = RentalRepository.rentals_data_list(self)
        for rental in rentals_list:
            file.write(self._rental_string(rental) + "\n")
        file.close()

    def add_rental(self, rental):
        RentalRepository.add_rental(self, rental)
        self._save_file()

    def return_book(self, rental_id, return_date):
        RentalRepository.return_book(self, rental_id, return_date)
        self._save_file()

    def delete_rental(self, rental_id):
        RentalRepository.delete_rental(self, rental_id)
        self._save_file()
