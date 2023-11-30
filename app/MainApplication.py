from re import I
import re

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QFileDialog,
    QHBoxLayout,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from app.MainApplicationWidget import MainApplicationWidget


class MainApplication(QMainWindow):
    def __init__(self, state):
        super().__init__()
        self.state = state
        self.setupMainWindow()
        self.centralWidget: QWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)
        self.centralLayout = QVBoxLayout(self.centralWidget)
        self.setupNavBar()
        self.setupMainWidget()
        self.setupActions()

    def setupMainWindow(self):
        self.setWindowTitle("Zombielers Desktop")
        self.setWindowState(Qt.WindowState.WindowMaximized)

    def setupNavBar(self):
        self.navBarLayout = QHBoxLayout()
        self.openFileButton = QPushButton("Open file")
        self.saveFileButton = QPushButton("Save file")
        self.navBarLayout.addWidget(self.openFileButton)
        self.navBarLayout.addWidget(self.saveFileButton)
        self.navBarLayout.addStretch()
        self.doAnalysisButton = QPushButton("Compile")
        self.doAnalysisButton.setStyleSheet("background-color: #BF4342")
        self.navBarLayout.addWidget(self.doAnalysisButton)
        self.navBarLayout.addStretch()
        # self.toggleLexerButton = QPushButton("Lexical")
        # self.toggleParserButton = QPushButton("Parser")
        # self.toggleSemanticButton = QPushButton("Semantic")
        # self.navBarLayout.addWidget(self.toggleLexerButton)
        # self.navBarLayout.addWidget(self.toggleParserButton)
        # self.navBarLayout.addWidget(self.toggleSemanticButton)
        self.navBar = QWidget(self)
        self.navBar.setLayout(self.navBarLayout)
        self.centralLayout.addWidget(self.navBar)

    def setupMainWidget(self):
        self.mainWidget = MainApplicationWidget(self.state)
        self.centralLayout.addWidget(self.mainWidget)

    def setupActions(self):
        self.openFileButton.clicked.connect(self.openFile)
        self.saveFileButton.clicked.connect(self.saveFile)
        self.doAnalysisButton.clicked.connect(self.mainWidget.compile)
        # self.toggleLexerButton.clicked.connect(self.mainWidget.toggleLexer)
        # self.toggleParserButton.clicked.connect(self.mainWidget.toggleSyntax)
        # self.toggleSemanticButton.clicked.connect(self.mainWidget.toggleSemantic)

    def openFile(self):
        fileName, _ = QFileDialog.getOpenFileName(
            self, "Open", "", "Text files (*.txt)"
        )
        if not fileName:
            messageBox = QMessageBox()
            messageBox.setWindowTitle("Warning")
            messageBox.setText("File not opened")
            messageBox.exec()
            return

        with open(fileName, "r") as file:
            text = file.read()
            self.mainWidget.setCode(text)

    def saveFile(self):
        fileName, _ = QFileDialog.getSaveFileName(
            self, "Save", "", "Text files (*.txt)"
        )
        if not fileName:
            # send warning to user with QMessageBox
            messageBox = QMessageBox()
            messageBox.setWindowTitle("Warning")
            messageBox.setText("File not saved")
            messageBox.exec()
            return

        with open(fileName, "w") as file:
            file.write(self.mainWidget.code)
