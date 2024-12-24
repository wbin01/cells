#!/usr/bin/env python3
from PySide6 import QtWidgets
from __feature__ import snake_case


class CoreLabel(QtWidgets.QLabel):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._obj = self
        self.set_object_name('Label')
        self.set_contents_margins(0, 0, 0, 0)
