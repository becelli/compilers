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

from frontend.custom_lexer import CustomLexer
from libraries.antlr.LALGErrorListener import LALGErrorListener
from libraries.antlr.LALGLexer import LALGLexer
from libraries.antlr.LALGParser import LALGParser


class Analyser(enum.Enum):
    LEXER = "lexer"
    SYNTAX = "syntax"
    SEMANTIC = "semantic"


class ApplicationWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._setupMainLayout()
        self._setupEditor()
        self._setupTableLexer()
        self._setupOutputs()
        self._updateLabel(Analyser.LEXER)

    def _setupMainLayout(self):
        self.editorLayout = QVBoxLayout()
        self.tableAndErrorsLayout = QVBoxLayout()
        self.mainLayout = QHBoxLayout()
        self.mainLayout.addLayout(self.editorLayout)
        self.mainLayout.addLayout(self.tableAndErrorsLayout)
        self.setLayout(self.mainLayout)

    def _setupEditor(self):
        self.textEditor = QsciScintilla(self)
        lexerElement = CustomLexer(self.textEditor)
        self.textEditor.setLexer(lexerElement)
        self.textEditor.setMarginLineNumbers(1, True)
        font = QFont("monospace", 16)
        self.textEditor.setFont(font)
        lexerElement.setFont(font)
        self.textEditor.setMarginsFont(font)
        self.editorLayout.addWidget(self.textEditor)

    def _setupTableLexer(self):
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

    def _setupOutputs(self):
        self.errTitle = QLabel()
        self.errOutput = self._createOutput()
        self.errorLayout = self._createOutputLayout(
            self.errTitle, self.errOutput)
        self.tableAndErrorsLayout.addLayout(self.errorLayout)

    def _createOutput(self):
        output = QTextEdit()
        output.setReadOnly(True)
        output.setFixedHeight(100)
        return output

    def _createOutputLayout(self, title, output):
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

    def analyze(self):
        """Analyze the current code."""
        self.lex()
        self.syntaxAnalysis()

    def lex(self):
        """Lexical analysis of the code."""
        stream = InputStream(self.code)
        lexer = LALGLexer(stream)
        tokens = lexer.getAllTokens()

        token_list = [
            [token.text, lexer.symbolicNames[token.type], token.line,
             token.column, token.column + len(token.text)]
            for token in tokens
        ]

        self._updateLexerTable(token_list)

    def _updateLexerTable(self, token_list):
        self.table.setRowCount(len(token_list))
        for i, token in enumerate(token_list):
            for j, value in enumerate(token):
                self.table.setItem(i, j, QTableWidgetItem(str(value)))

    def syntaxAnalysis(self):
        """Syntactical analysis of the code."""
        input_stream = InputStream(self.code)
        lexer = LALGLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = LALGParser(token_stream)

        parser.removeErrorListeners()
        parser.addErrorListener(LALGErrorListener())
        parser.variable()

        errors = parser.getErrors()
        self.errOutput.clear()
        for error in errors:
            self.errOutput.append(error)

    def toggleLexer(self):
        self._updateLabel(Analyser.LEXER)

    def toggleSyntax(self):
        self._updateLabel(Analyser.SYNTAX)

    def toggleSemantic(self):
        self._updateLabel(Analyser.SEMANTIC)

    def _updateLabel(self, analyser: Analyser = Analyser.LEXER):
        match analyser:
            case Analyser.LEXER:
                self.errTitle.setText("Lexer Errors")
            case Analyser.SYNTAX:
                self.errTitle.setText("Syntax Errors")
            case Analyser.SEMANTIC:
                self.errTitle.setText("Semantic Errors")
