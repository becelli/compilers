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

from compiler.ErrorListener import ErrorListener
from compiler.LangLexer import LangLexer
from compiler.LangParser import LangParser
from frontend.custom_lexer import CustomLexer

class ApplicationWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._setupCentralLayout()
        self._setupEditor()
        self._setupButton()
        self._setupTable()
        self._setupOutputs()

    def _setupCentralLayout(self):
        self.centralLayout = QVBoxLayout()
        self.edAndTableLay = QHBoxLayout()
        self.bottomLayout = QHBoxLayout()
        
        self.centralLayout.addLayout(self.edAndTableLay)
        self.centralLayout.addLayout(self.bottomLayout)
        self.centralLayout.setStretch(0, 1)
        
        self.setLayout(self.centralLayout)

    def _setupEditor(self):
        self.textEditor = QsciScintilla(self)
        lexerElement = CustomLexer(self.textEditor) # type: ignore
        self.textEditor.setLexer(lexerElement)
        self.textEditor.setMarginLineNumbers(1, True)
        
        font = QFont("monospace", 16)
        self.textEditor.setFont(font)
        lexerElement.setFont(font)
        self.textEditor.setMarginsFont(font)
        
        self.edAndTableLay.addWidget(self.textEditor)

    def _setupButton(self):
        self.button = QPushButton("Analisar", self)
        self.button.clicked.connect(self.analyze)

        btnsLayout = QVBoxLayout()
        btnsLayout.addStretch()
        btnsLayout.addWidget(self.button)
        self.bottomLayout.addLayout(btnsLayout)

    def _setupTable(self):
        self.table = QTableWidget(1, 5, self)
        horizontalHeader = self.table.horizontalHeader()
        if horizontalHeader is not None:
            horizontalHeader.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table.setHorizontalHeaderLabels(["Lexema", "Token", "Linha", "Col. inicial", "Col. final"])
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)

        self.edAndTableLay.addWidget(self.table)

    def _setupOutputs(self):
        lexTitle = QLabel("<b>Erros Léxicos</b>")
        self.lexOutput = self._createOutput()
        
        sinTitle = QLabel("<b>Erros Sintáticos</b>")
        self.sinOutput = self._createOutput()

        lexLayout = self._createOutputLayout(lexTitle, self.lexOutput)
        sinLayout = self._createOutputLayout(sinTitle, self.sinOutput)

        self.bottomLayout.addLayout(lexLayout)
        self.bottomLayout.addLayout(sinLayout)

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
        lexer = LangLexer(stream)
        tokens = lexer.getAllTokens()

        token_list = [
            [token.text, lexer.symbolicNames[token.type], token.line, 
             token.column, token.column + len(token.text)] 
            for token in tokens
        ]
        
        self._updateTable(token_list)

    def _updateTable(self, token_list):
        self.table.setRowCount(len(token_list))
        for i, token in enumerate(token_list):
            for j, value in enumerate(token):
                self.table.setItem(i, j, QTableWidgetItem(str(value)))

    def syntaxAnalysis(self):
        """Syntactical analysis of the code."""
        input_stream = InputStream(self.code)
        lexer = LangLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = LangParser(token_stream)
        
        parser.removeErrorListeners()
        parser.addErrorListener(ErrorListener())
        parser.variavel()
        
        # TODO: retornar erros no parser
        # errors = parser.getErrors()
        self.sinOutput.clear()
        # for error in errors:
        #     self.sinOutput.append(error)
