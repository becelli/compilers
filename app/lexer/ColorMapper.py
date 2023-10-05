from dataclasses import dataclass

from PyQt6.QtGui import QColor

from app.lexer.Colors import Colors


@dataclass
class ColorMapper:
    @staticmethod
    def getColor(style: Colors) -> QColor:
        mapper = {
            Colors.primaryStyle.value: QColor("#242424"),
            Colors.secondaryStyle.value: QColor("#c01c28"),
            Colors.commentStyle.value: QColor("#8ff0a4"),
            Colors.backgroundStyle.value: QColor("#ffffff"),
            Colors.foregroundStyle.value: QColor("#242424"),
            Colors.lowContrastStyle.value: QColor("#a0a0a0"),
        }
        return mapper[style.value]
