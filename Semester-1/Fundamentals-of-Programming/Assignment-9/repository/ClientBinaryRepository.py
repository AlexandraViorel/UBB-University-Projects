from src.repository.ClientRepository import ClientRepository
from src.domain.exceptions import FileException
import pickle


class ClientBinaryRepository(ClientRepository):
    def __init__(self, file_name):
        ClientRepository.__init__(self)
        self._file_name = file_name
        self._load_file()

    def _load_file(self):
        try:
            file = open(self._file_name, "rb")
        except IOError:
            raise FileException("Error! File not found!")
        try:
            clients_list = pickle.load(file)
            for client in clients_list:
                ClientRepository.add_client(self, client)
        except EOFError:
            ClientRepository.__init__(self, dict())
        file.close()

    def _save_file(self):
        file = open(self._file_name, "wb")
        clients_list = ClientRepository.clients_data_list(self)
        pickle.dump(clients_list, file)
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
