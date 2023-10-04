import sys

from PyQt6.QtWidgets import QApplication

from app.MainApplication import MainApplication
from state.AppState import AppState


def setup():
    state = AppState()
    app = QApplication(sys.argv)
    window = MainApplication(state)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    setup()
