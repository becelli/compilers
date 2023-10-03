from re import I

from PyQt6.QtWidgets import QFileDialog, QPushButton, QMainWindow, QHBoxLayout, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt

from frontend.application_widget import ApplicationWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Zombielers Desktop")
        self.setWindowState(Qt.WindowState.WindowMaximized)
        self.centralWidget: QWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)
        self.centralLayout = QVBoxLayout(self.centralWidget)
        self._setupNavBar()
        self._setupMainWidget()

    def _setupNavBar(self):
        self.navBarLayout = QHBoxLayout()
        self.openFileButton = QPushButton("Open file")
        self.openFileButton.clicked.connect(self.openFile)
        self.saveFileButton = QPushButton("Save file")
        self.saveFileButton.clicked.connect(self.saveFile)
        self.navBarLayout.addWidget(self.openFileButton)
        self.navBarLayout.addWidget(self.saveFileButton)
        self.navBarLayout.addStretch()
        self.doAnalysisButton = QPushButton("Analyze")
        self.doAnalysisButton.setStyleSheet("background-color: red")
        self.navBarLayout.addWidget(self.doAnalysisButton)
        self.navBarLayout.addStretch()
        self.toggleLexerButton = QPushButton("Lexical")
        self.toggleParserButton = QPushButton("Parser")
        self.toggleSemanticButton = QPushButton("Semantic")
        self.navBarLayout.addWidget(self.toggleLexerButton)
        self.navBarLayout.addWidget(self.toggleParserButton)
        self.navBarLayout.addWidget(self.toggleSemanticButton)
        self.navBar = QWidget(self)
        self.navBar.setLayout(self.navBarLayout)
        self.centralLayout.addWidget(self.navBar)

    def _setupMainWidget(self):
        self.mainWidget = ApplicationWidget()
        self.centralLayout.addWidget(self.mainWidget)

    def openFile(self):
        fileName, _ = QFileDialog.getOpenFileName(
            self, "Abrir arquivo", "", "Arquivo de texto (*.txt)")
        if fileName:
            with open(fileName, "r") as file:
                text = file.read()
                self.mainWidget.setCode(text)

    def saveFile(self):
        fileName, _ = QFileDialog.getSaveFileName(
            self, "Salvar arquivo", "", "Arquivo de texto (*.txt)")
        if fileName:
            with open(fileName, "w") as file:
                pass
                # file.write(self.mainWidget.code())
