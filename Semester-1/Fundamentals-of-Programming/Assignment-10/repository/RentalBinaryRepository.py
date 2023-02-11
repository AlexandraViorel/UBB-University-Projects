from src.repository.RentalRepository import RentalRepository
from src.domain.exceptions import FileException
import pickle


class RentalBinaryRepository(RentalRepository):
    def __init__(self, file_name):
        RentalRepository.__init__(self)
        self._file_name = file_name
        self._load_file()

    def _load_file(self):
        try:
            file = open(self._file_name, "rb")
        except IOError:
            raise FileException("Error! File not found!")
        try:
            rentals_list = pickle.load(file)
            for rental in rentals_list:
                RentalRepository.add_rental(self, rental)
        except EOFError:
            RentalRepository.__init__(self, dict())
        file.close()

    def _save_file(self):
        file = open(self._file_name, "wb")
        rentals_list = RentalRepository.rentals_data_list(self)
        pickle.dump(rentals_list, file)
        file.close()

    def add_rental(self, rental):
        RentalRepository.add_rental(self, rental)
        self._save_file()

    def delete_rental(self, rental_id):
        RentalRepository.delete_rental(self, rental_id)
        self._save_file()

    def return_book(self, rental_id, return_date):
        RentalRepository.return_book(self, rental_id, return_date)
        self._save_file()
