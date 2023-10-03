from dataclasses import dataclass
from enum import Enum
import re

from PyQt6.Qsci import QsciLexerCustom, QsciScintilla
from PyQt6.QtGui import QColor, QFont

class Colors(Enum):
    primaryStyle = 0
    secondaryStyle = 1
    commentStyle = 2
    backgroundStyle = 3
    foregroundStyle = 4

@dataclass
class ColorMapper:
    @staticmethod
    def getColor(style: Colors) -> QColor:
        mapper = {
            Colors.primaryStyle.value: QColor("#f8f8f2"),
            Colors.secondaryStyle.value: QColor("#ff79c6"),
            Colors.commentStyle.value: QColor("#6272a4"),
            Colors.backgroundStyle.value: QColor("#282a36"),
            Colors.foregroundStyle.value: QColor("#f8f8f2")
        }
        return mapper[style.value]


class CustomLexer(QsciLexerCustom):
    reservedKeywords = { 
        "program", "procedure", "var", "int", "boolean", "read", "write", "true", 
        "false", "begin", "end", "if", "then", "else", "or", "and", "not", "div", 
        "while", "do"
    }

    startMultilineCommentTokens = "{"
    endMultilineCommentTokens = "}"
    startCommentTokens = ["//", startMultilineCommentTokens]
    
    def __init__(self, parent: QsciScintilla):
        super().__init__(parent)
        self.initializeStyles()

    def initializeStyles(self):
        self.setDefaultColor(ColorMapper.getColor(Colors.foregroundStyle))
        self.setDefaultPaper(ColorMapper.getColor(Colors.backgroundStyle))

        for style in Colors:
            self.setColor(ColorMapper.getColor(style), style.value)
            self.setPaper(ColorMapper.getColor(Colors.backgroundStyle), style.value)

    def description(self, styleNumber: int) -> str:
        styleDescriptions = {
            Colors.primaryStyle.value: "black",
            Colors.secondaryStyle.value: "blue",
            Colors.commentStyle.value: "red"
        }
        return styleDescriptions.get(styleNumber, "")

    def defaultFont(self, style: int) -> QFont:
        return QFont("monospace", 24, QFont.Weight.Bold)

    def styleText(self, startPos: int, endPos: int):
        self.startStyling(0)
        textContent = self.parent().text() # type: ignore
        tokenList = [
            (token, len(bytearray(token, "utf-8")))
            for token in re.findall(r"\s+|\w+|\/\/|\W", textContent)
        ]

        inComment = False
        inMultilineComment = False

        for token, tokenLength in tokenList:
            if inComment:
                self.setStyling(tokenLength, Colors.commentStyle.value)
                if inMultilineComment:
                    if token == self.endMultilineCommentTokens:
                        inMultilineComment = False
                        inComment = False
                else:
                    if token[-1] in ["\n", "\r"]:
                        inComment = False
            else:
                if token in self.reservedKeywords:
                    self.setStyling(tokenLength, Colors.secondaryStyle.value)
                elif token in self.startMultilineCommentTokens:
                    self.setStyling(tokenLength, Colors.commentStyle.value)
                    if token == "{":
                        inMultilineComment = True
                    inComment = True
                else:
                    self.setStyling(tokenLength, Colors.primaryStyle.value)
