import re
from PyQt6.Qsci import QsciLexerCustom
from PyQt6.QtGui import QFont, QColor
from dataclasses import dataclass
from enum import Enum

class Colors(Enum):
    PRIMARY_STYLE = 0
    SECONDARY_STYLE = 1
    COMMENT_STYLE = 2
    BACKGROUND_STYLE = 3
    FOREGROUND_STYLE = 4

@dataclass
class ColorMapper:
    @staticmethod
    def get_color(style: Colors) -> QColor:
        mapper = {
            Colors.PRIMARY_STYLE.value: QColor("#f8f8f2"),
            Colors.SECONDARY_STYLE.value: QColor("#ff79c6"),
            Colors.COMMENT_STYLE.value: QColor("#6272a4"),
            Colors.BACKGROUND_STYLE.value: QColor("#282a36"),
            Colors.FOREGROUND_STYLE.value: QColor("#f8f8f2")
        }
        return mapper[style.value]


class CustomLexer(QsciLexerCustom):
    RESERVED_KEYWORDS = { 
        "program", "procedure", "var", "int", "boolean", "read", "write", "true", 
        "false", "begin", "end", "if", "then", "else", "or", "and", "not", "div", 
        "while", "do"
    }

    COMMENT_TOKENS = ["//", "{"]
    
    def __init__(self, parent: QsciLexerCustom):
        super().__init__(parent)
        self._initialize_styles()

    def _initialize_styles(self):
        self.setDefaultColor(ColorMapper.get_color(Colors.FOREGROUND_STYLE))
        self.setDefaultPaper(ColorMapper.get_color(Colors.BACKGROUND_STYLE))

        for style in Colors:
            self.setColor(ColorMapper.get_color(style), style.value)
            self.setPaper(ColorMapper.get_color(Colors.BACKGROUND_STYLE), style.value)

    def description(self, style_number: int) -> str:
        style_descriptions = {
            Colors.PRIMARY_STYLE.value: "black",
            Colors.SECONDARY_STYLE.value: "blue",
            Colors.COMMENT_STYLE.value: "red"
        }
        return style_descriptions.get(style_number, "")

    def defaultFont(self, _style: int) -> QFont:
        return QFont("monospace", 24, QFont.Weight.Bold)

    def styleText(self, _start_pos: int, _end_pos: int):
        self.startStyling(0)
        text_content = self.parent().text() # type: ignore
        token_list = [
            (token, len(bytearray(token, "utf-8")))
            for token in re.findall(r"\s+|\w+|\/\/|\W", text_content)
        ]

        in_comment = False
        in_multiline_comment = False

        for token, token_length in token_list:
            if in_comment:
                self.setStyling(token_length, Colors.COMMENT_STYLE.value)
                if in_multiline_comment:
                    if token == "}":
                        in_multiline_comment = False
                        in_comment = False
                else:
                    if token[-1] in ["\n", "\r"]:
                        in_comment = False
            else:
                if token in self.RESERVED_KEYWORDS:
                    self.setStyling(token_length, Colors.SECONDARY_STYLE.value)
                elif token in self.COMMENT_TOKENS:
                    self.setStyling(token_length, Colors.COMMENT_STYLE.value)
                    if token == "{":
                        in_multiline_comment = True
                    in_comment = True
                else:
                    self.setStyling(token_length, Colors.PRIMARY_STYLE.value)
