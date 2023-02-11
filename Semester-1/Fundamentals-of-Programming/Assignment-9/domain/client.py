import random

CLIENTS_NAMES = ["Alexandra", "Andrei", "Maria", "Marius", "Flaviu", "Vlad", "Georgiana", "Andreea", "Paul"]


class Client:
    def __init__(self, client_id, name):
        self._client_id = client_id
        self._name = name

    @property
    def client_id(self):
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        self._client_id = client_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def __str__(self):
        return "Client id: " + str(self._client_id) + ", Name: " + self._name

    def object_to_dictionary(self):
        return {"client_id": self.client_id, "name": self.name}


def generate_random_clients(n=20):
    clients_data = {}
    random_client = Client(1, "Alexandra")
    clients_data[1] = random_client
    for i in range(2, n+1):
        client_id = i
        client_name = CLIENTS_NAMES[random.randint(0, 8)]
        random_generated_client = Client(client_id, client_name)
        clients_data[client_id] = random_generated_client
    return clients_data
