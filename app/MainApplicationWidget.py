from PyQt6.Qsci import QsciScintilla
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QTableWidget,
    QTableWidgetItem,
    QTextEdit,
    QVBoxLayout,
    QWidget,
    QSizePolicy,
)
from antlr4 import CommonTokenStream, InputStream
from app.entities.CompilerSteps import CompilerSteps
from app.lexer.ColorMapper import ColorMapper
from app.lexer.Colors import Colors
from app.lexer.CustomLexer import CustomLexer
from libraries.antlr.custom.LALGCodeGenerator import LALGCodeGenerator
from libraries.antlr.custom.LALGCustomErrorStrategy import LALGCustomErrorStrategy
from libraries.antlr.custom.LALGErrorListener import LALGErrorListener
from libraries.antlr.LALGLexer import LALGLexer
from libraries.antlr.LALGParser import LALGParser
from libraries.interpreter.LALGCodeInterpreter import LALGCodeInterpreter
from libraries.state.AppState import AppState
from libraries.antlr.custom.LALGSemanticAnalyzer import LALGSemanticAnalyzer


class MainApplicationWidget(QWidget):
    def __init__(self, state: AppState):
        super().__init__()
        self.state = state
        self.setupMainLayout()
        self.setupEditor()
        self.setupTableLexer()
        self.setupOutputs()

        # make elements in tableAndErrorsLayout to expand
        self.tableAndErrorsLayout.addStretch()

        self.is_running = False

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
        self.textEditor.setMarginsBackgroundColor(
            ColorMapper.getColor(Colors.backgroundStyle)
        )
        self.textEditor.setMarginsForegroundColor(
            ColorMapper.getColor(Colors.lowContrastStyle)
        )

        self.textEditor.setMarginWidth(1, "0000000")
        self.textEditor.setMarginWidth(2, "000000")

        font = QFont("monospace", 16)
        self.textEditor.setFont(font)
        lexerElement.setFont(font)
        self.textEditor.setMarginsFont(font)
        self.editorLayout.addWidget(self.textEditor)

    def setupTableLexer(self):
        self.table = QTableWidget(0, 5, self)
        horizontalHeader = self.table.horizontalHeader()
        if horizontalHeader is not None:
            horizontalHeader.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table.setHorizontalHeaderLabels(
            ["Lexem", "Token", "Line", "Start Column", "End Column"]
        )
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.table.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)

        # self.table.setSizePolicy(
        #     QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        # )
        # self.table.setSizeAdjustPolicy(QTableWidget.SizeAdjustPolicy.AdjustToContents)

        self.tableAndErrorsLayout.addWidget(self.table, 1)

    def setupOutputs(self):
        self.outputErrorType = QLabel("Errors")
        self.outputError = self.createOutput()
        self.errorLayout = self.createOutputLayout(
            self.outputErrorType, self.outputError
        )

        # self.outputError.setSizePolicy(
        #     QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        # )
        # self.outputError.setSizeAdjustPolicy(
        #     QTextEdit.SizeAdjustPolicy.AdjustToContents
        # )
        self.tableAndErrorsLayout.addLayout(self.errorLayout, 1)

    def createOutput(self) -> QTextEdit:
        output = QTextEdit()
        output.setReadOnly(True)
        return output

    def createOutputLayout(self, title: QLabel, output: QTextEdit) -> QVBoxLayout:
        layout = QVBoxLayout()
        layout.addStretch()
        layout.addWidget(title)
        layout.addWidget(output, 1)
        layout.setContentsMargins(0, 0, 0, 0)
        return layout

    def setCode(self, code: str):
        self.textEditor.setText(code)

    @property
    def code(self) -> str:
        return self.textEditor.text()

    def updateLexerTable(self, token_list):
        self.table.setRowCount(len(token_list))
        for row, token in enumerate(token_list):
            for col, value in enumerate(token):
                self.table.setItem(row, col, QTableWidgetItem(str(value)))

    def compile(self):
        if self.is_running:
            return
        self.outputError.clear()
        listener = LALGErrorListener(self.outputError)
        self.lexicalAnalysis(listener)
        self.syntaxAnalysis(listener)

    def lexicalAnalysis(self, listener: LALGErrorListener):
        lexer = LALGLexer(InputStream(self.code))
        tokens = lexer.getAllTokens()
        tokenList = [
            [
                token.text,
                lexer.symbolicNames[token.type],
                token.line,
                token.column,
                token.column + len(token.text),
            ]
            for token in tokens
        ]

        self.updateLexerTable(tokenList)

        for token in tokens:
            if token.type in [LALGLexer.INVALID, LALGLexer.INVALID_TOKEN]:
                message = f"unexpected character: {token.text}"
                listener.lexerError(token.line, token.column, message)

    def syntaxAnalysis(self, listener: LALGErrorListener):
        lexer = LALGLexer(InputStream(self.code))
        tokens = CommonTokenStream(lexer)
        parser = LALGParser(tokens)

        lexer.removeErrorListeners()
        parser.removeErrorListeners()
        lexer.addErrorListener(listener)
        parser.addErrorListener(listener)
        parser._errHandler = LALGCustomErrorStrategy()

        tree = parser.program()

        if parser.getNumberOfSyntaxErrors() > 0:
            return

        semanticAnalyzer = LALGSemanticAnalyzer(listener)
        semanticAnalyzer.visit(tree)

        if listener.hasErrors:
            return

        self.is_running = True
        codeGenerator = LALGCodeGenerator()
        code = codeGenerator.generate(tree)
        interpreter = LALGCodeInterpreter(code)
        interpreter.run()
        self.is_running = False
