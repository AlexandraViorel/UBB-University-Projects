from ui import UI
from settings import Settings


try:
    if Settings().ui_type() == "ui":
        UI().start()
except Exception as message:
    print(str(message))
