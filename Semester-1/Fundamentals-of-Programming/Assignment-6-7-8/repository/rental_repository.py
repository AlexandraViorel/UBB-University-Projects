from src.domain.rental import generate_random_rentals
import datetime


class RentalRepository:
    def __init__(self):
        self._rentals_data = generate_random_rentals()

    def rentals_data_list(self):
        return list(self._rentals_data.values())

    def __setitem__(self, key, value):
        self._rentals_data[key] = value

    def __delitem__(self, key):
        del self._rentals_data[key]

    def __len__(self):
        return len(self._rentals_data)

    def length_of_rental(self, rental_id):
        if self._rentals_data[int(rental_id)].returned_date is None:
            today = datetime.date.today()
            rental_date = self._rentals_data[int(rental_id)].rented_date
            return (today-rental_date).days + 1
        return_date = self._rentals_data[int(rental_id)].returned_date
        rental_date = self._rentals_data[int(rental_id)].rented_date
        return (return_date - rental_date).days + 1

    def add_rental(self, given_rental):
        self._rentals_data[int(given_rental.rental_id)] = given_rental

    def return_book(self, rental_id, return_date):
        self._rentals_data[int(rental_id)].returned_date = return_date

    def delete_rental(self, rental_id):
        del self._rentals_data[rental_id]
