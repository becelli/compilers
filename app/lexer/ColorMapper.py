from dataclasses import dataclass

from PyQt6.QtGui import QColor

from app.lexer.Colors import Colors

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
