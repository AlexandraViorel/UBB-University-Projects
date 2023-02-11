from configparser import ConfigParser


class Settings:
    def __init__(self):
        self._parser = ConfigParser()
        self._parser.read("settings.ini")

    def who_moves_first(self):
        who_moves_first = self._parser.get("settings", "first")
        return who_moves_first

    def ai_type(self):
        ai_type = self._parser.get("settings", "difficulty")
        return ai_type

    def ui_type(self):
        ui_type = self._parser.get("settings", "ui")
        return ui_type
