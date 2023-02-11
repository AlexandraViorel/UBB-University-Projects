from src.domain.client import Client
from src.repository.ClientRepository import ClientRepository
from src.domain.exceptions import FileException
import json


class ClientJSONRepository(ClientRepository):
    def __init__(self, file_name):
        ClientRepository.__init__(self)
        self._file_name = file_name
        self._load_file()

    def _load_file(self):
        try:
            file = open(self._file_name, "r")
        except IOError:
            raise FileException("Error! File not found!")
        try:
            clients_list = json.load(file)
            for client in clients_list:
                ClientRepository.add_client(self, Client(client["client_id"], client["name"]))
        except json.JSONDecodeError:
            ClientRepository.__init__(self, dict())
        file.close()

    def _list_of_client_dictionaries(self):
        clients_list = ClientRepository.clients_data_list(self)
        clients_dictionaries_list = []
        for client in clients_list:
            clients_dictionaries_list.append(client.object_to_dictionary())
        return clients_dictionaries_list

    def _save_file(self):
        clients_dictionaries_list = self._list_of_client_dictionaries()
        file = open(self._file_name, "w")
        json.dump(clients_dictionaries_list, file)
        file.close()

    def add_client(self, client):
        ClientRepository.add_client(self, client)
        self._save_file()

    def remove_client(self, client_id):
        ClientRepository.remove_client(self, client_id)
        self._save_file()

    def update_client(self, updated_client):
        ClientRepository.update_client(self, updated_client)
        self._save_file()
