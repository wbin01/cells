#!/usr/bin/env python3
from PySide6 import QtWidgets
from __feature__ import snake_case

from .component import Component


class Label(Component):
    def __init__(self, text: str = '', *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.qt_obj = QtWidgets.QLabel(text)

    @property
    def text(self) -> str:
        """..."""
        return self.qt_obj.text()

    @text.setter
    def text(self, text: str) -> None:
        """..."""
        self.qt_obj.set_text(text)
