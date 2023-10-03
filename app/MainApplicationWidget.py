import enum

from PyQt6.Qsci import QsciScintilla
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)
from antlr4 import CommonTokenStream, InputStream
from app.entities.CompilerSteps import CompilerSteps

from app.lexer.CustomLexer import CustomLexer
from libraries.antlr.LALGErrorListener import LALGErrorListener
from libraries.antlr.LALGLexer import LALGLexer
from libraries.antlr.LALGParser import LALGParser


class MainApplicationWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setupMainLayout()
        self.setupEditor()
        self.setupOutputs()
        self.setupTableLexer()
        self.toggleLexer()

    def setupMainLayout(self):
        self.editorLayout = QVBoxLayout()
        self.tableAndErrorsLayout = QVBoxLayout()
        self.mainLayout = QHBoxLayout()
        self.mainLayout.addLayout(self.editorLayout)
        self.mainLayout.addLayout(self.tableAndErrorsLayout)
        self.setLayout(self.mainLayout)

    def setupEditor(self):
        self.textEditor = QsciScintilla(self)
        lexerElement = CustomLexer(self.textEditor)
        self.textEditor.setLexer(lexerElement)
        self.textEditor.setMarginLineNumbers(1, True)
        font = QFont("monospace", 16)
        self.textEditor.setFont(font)
        lexerElement.setFont(font)
        self.textEditor.setMarginsFont(font)
        self.editorLayout.addWidget(self.textEditor)

    def setupTableLexer(self):
        self.table = QTableWidget(1, 5, self)
        horizontalHeader = self.table.horizontalHeader()
        if horizontalHeader is not None:
            horizontalHeader.setSectionResizeMode(
                QHeaderView.ResizeMode.Stretch)
        self.table.setHorizontalHeaderLabels(
            ["Lexem", "Token", "Line", "Start Column", "End Column"])
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.table.setSelectionBehavior(
            QTableWidget.SelectionBehavior.SelectRows)

        self.tableAndErrorsLayout.addWidget(self.table)        

    def setupOutputs(self):
        self.errTitle = QLabel()
        self.outputError = self.createOutput()
        self.errorLayout = self.createOutputLayout(self.errTitle, self.outputError)
        self.tableAndErrorsLayout.addLayout(self.errorLayout)

    def createOutput(self):
        output = QTextEdit()
        output.setReadOnly(True)
        return output

    def createOutputLayout(self, title, output):
        layout = QVBoxLayout()
        layout.addStretch()
        layout.addWidget(title)
        layout.addWidget(output)
        return layout

    def setCode(self, code: str):
        self.textEditor.setText(code)

    @property
    def code(self) -> str:
        return self.textEditor.text()

    def lex(self):
        stream = InputStream(self.code)
        lexer = LALGLexer(stream)
        tokens = lexer.getAllTokens()

        token_list = [
            [token.text, lexer.symbolicNames[token.type], token.line,
             token.column, token.column + len(token.text)]
            for token in tokens
        ]

        self.updateLexerTable(token_list)

    def updateLexerTable(self, token_list):
        self.table.setRowCount(len(token_list))
        for row, token in enumerate(token_list):
            for col, value in enumerate(token):
                self.table.setItem(row, col, QTableWidgetItem(str(value)))

    def analyze(self):
        self.lex()
        self.syntaxAnalysis()

    def syntaxAnalysis(self):
        input_stream = InputStream(self.code)
        lexer = LALGLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = LALGParser(token_stream)

        listener = LALGErrorListener()
        parser.removeErrorListeners()
        parser.addErrorListener(listener)

        parser.variable()

        errors = listener.getErrors()
        self.outputError.clear()
        for error in errors:
            self.outputError.append(error)
        

    def toggleLexer(self):
        self.updateLabel(CompilerSteps.LEXER)

    def toggleSyntax(self):
        self.updateLabel(CompilerSteps.SYNTAX)

    def toggleSemantic(self):
        self.updateLabel(CompilerSteps.SEMANTIC)

    def updateLabel(self, CompilerSteps: CompilerSteps = CompilerSteps.LEXER):
        match CompilerSteps:
            case CompilerSteps.LEXER:
                self.errTitle.setText("Lexer Errors")
            case CompilerSteps.SYNTAX:
                self.errTitle.setText("Syntax Errors")
            case CompilerSteps.SEMANTIC:
                self.errTitle.setText("Semantic Errors")
