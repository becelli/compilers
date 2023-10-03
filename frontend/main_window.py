from re import I

from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QFileDialog, QMainWindow, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt

from frontend.application_widget import ApplicationWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self._setupMainWindow()
        self._setupCentralWidget()
        self._setupMenuBar()
        self._setupMainWidget()

    def _setupMainWindow(self):
        self.setWindowTitle("Zombielers Desktop")
        self.setWindowState(Qt.WindowState.WindowMaximized)

    def _setupCentralWidget(self):
        self.centralWidget: QWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)
        self.centralLayout = QVBoxLayout(self.centralWidget)
    
    def _setupMenuBar(self):
        menuBar = self.menuBar()
        if menuBar is None:
            return
        
        fileMenu = menuBar.addMenu("Opções")
        if fileMenu is None:
            return

        fileMenu.addAction(self._createAction("Abrir código", "Ctrl+O", self.openFile))
        fileMenu.addAction(self._createAction("Salvar código", "Ctrl+S", self.saveFile))
    
    def _createAction(self, title, shortcut, slot):
        action = QAction(title, self)
        action.setShortcut(shortcut)
        action.triggered.connect(slot)
        return action

    def _setupMainWidget(self):
        self.mainWidget = ApplicationWidget()
        self.centralLayout.addWidget(self.mainWidget)
        
    def openFile(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Abrir arquivo", "", "Arquivo de texto (*.txt)")
        if fileName:
            with open(fileName, "r") as file:
                text = file.read()
                self.mainWidget.setCode(text)

    def saveFile(self):
        fileName, _ = QFileDialog.getSaveFileName(self, "Salvar arquivo", "", "Arquivo de texto (*.txt)")
        if fileName:
            with open(fileName, "w") as file:
                file.write(self.mainWidget.code())

