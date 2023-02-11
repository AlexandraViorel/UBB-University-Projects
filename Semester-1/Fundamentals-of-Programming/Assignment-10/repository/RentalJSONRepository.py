from src.domain.rental import Rental
from src.repository.RentalRepository import RentalRepository
from src.domain.exceptions import FileException
import json
import datetime


class RentalJSONRepository(RentalRepository):
    def __init__(self, file_name):
        RentalRepository.__init__(self)
        self._file_name = file_name
        self._load_file()

    def _load_file(self):
        try:
            file = open(self._file_name, "r")
        except IOError:
            raise FileException("Error! File not found!")
        try:
            rentals_dictionaries_list = json.load(file)
            for rental_dictionary in rentals_dictionaries_list:
                rented_year, rented_month, rented_day = rental_dictionary["rented_date"].split("-")
                rented_date = datetime.date(int(rented_year), int(rented_month), int(rented_day))
                if rental_dictionary["returned_date"] != "None":
                    return_year, return_month, return_day = rental_dictionary["returned_date"].split("-")
                    return_date = datetime.date(int(return_year), int(return_month), int(return_day))
                else:
                    return_date = None
                RentalRepository.add_rental(self, Rental(rental_dictionary["rental_id"], rental_dictionary["book_id"],
                                                         rental_dictionary["client_id"], rented_date, return_date))
        except json.JSONDecodeError:
            RentalRepository.__init__(self, dict())
        file.close()

    def _list_of_rental_dictionaries(self):
        rentals_list = RentalRepository.rentals_data_list(self)
        rentals_dictionaries_list = []
        for rental in rentals_list:
            rentals_dictionaries_list.append(rental.object_to_dictionary())
        return rentals_dictionaries_list

    def _save_file(self):
        rentals_dictionaries_list = self._list_of_rental_dictionaries()
        file = open(self._file_name, "w")
        json.dump(rentals_dictionaries_list, file)
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
