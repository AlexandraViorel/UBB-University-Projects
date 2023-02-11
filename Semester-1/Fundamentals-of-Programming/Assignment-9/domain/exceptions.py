class IdException(Exception):
    def __init__(self, error):
        self._error = error

    def __str__(self):
        return self._error


class FileException(Exception):
    def __init__(self, error):
        self._error = error

    def __str__(self):
        return self._error


class UndoRedoException(Exception):
    def __init__(self, error):
        self._error = error

    def __str__(self):
        return self._error


class DateException(Exception):
    def __init__(self, error):
        self._error = error

    def __str__(self):
        return self._error


class RepositoryException(Exception):
    def __init__(self, error):
        self._error = error

    def __str__(self):
        return self._error


class RentalException(Exception):
    def __init__(self, error):
        self._error = error

    def __str__(self):
        return self._error


class BookException(Exception):
    def __init__(self, error):
        self._error = error

    def __str__(self):
        return self._error


class BookValidatorExceptions(BookException):
    def __init__(self, errors_list):
        self._errors_list = errors_list

    def __str__(self):
        errors_to_print = ''
        for error in self._errors_list:
            errors_to_print += error
            errors_to_print += '\n'
        return errors_to_print


class ClientException(Exception):
    def __init__(self, error):
        self._error = error

    def __str__(self):
        return self._error


class ClientValidatorExceptions(ClientException):
    def __init__(self, errors_list):
        self._errors_list = errors_list

    def __str__(self):
        errors_to_print = ''
        for error in self._errors_list:
            errors_to_print += error
            errors_to_print += '\n'
        return errors_to_print
