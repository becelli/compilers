import sys

from PyQt6.QtWidgets import QApplication

from frontend.main_window import MainWindow

def setup():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    setup()