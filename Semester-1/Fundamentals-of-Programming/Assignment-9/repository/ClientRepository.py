class ClientRepository:
    def __init__(self, clients_data_dictionary=None):
        if clients_data_dictionary is None:
            clients_data_dictionary = {}
        self._clients_data = clients_data_dictionary

    def clients_data_list(self):
        return list(self._clients_data.values())

    def __setitem__(self, key, value):
        self._clients_data[key] = value

    def __delitem__(self, key):
        del self._clients_data[key]

    def __len__(self):
        return len(self._clients_data)

    def add_client(self, given_client):
        self._clients_data[int(given_client.client_id)] = given_client

    def remove_client(self, client_id):
        del self._clients_data[int(client_id)]

    def update_client(self, updated_client):
        self._clients_data[updated_client.client_id] = updated_client
