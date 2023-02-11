from src.domain.client import Client
from src.repository.ClientRepository import ClientRepository
from src.domain.exceptions import FileException


class ClientTextFileRepository(ClientRepository):
    def __init__(self, file_name):
        ClientRepository.__init__(self)
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
            client = Client(int(values[0]), values[1])
            ClientRepository.add_client(self, client)
            line = file.readline().strip()
        file.close()

    @staticmethod
    def _client_string(client):
        return str(client.client_id) + ";" + str(client.name)

    def _save_file(self):
        file = open(self._file_name, "w")
        clients_list = ClientRepository.clients_data_list(self)
        for client in clients_list:
            file.write(self._client_string(client) + "\n")
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
