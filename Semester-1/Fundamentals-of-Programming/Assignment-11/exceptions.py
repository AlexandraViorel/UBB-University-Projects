class ShipError(Exception):
    def __init__(self, error_message):
        self._error_message = error_message

    def __str__(self):
        return self._error_message


class BoardError(Exception):
    def __init__(self, error_message):
        self._error_message = error_message

    def __str__(self):
        return self._error_message
