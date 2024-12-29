#!/usr/bin/env python3
import os
import sys
import pprint

from cells import (
    Application, Cursor, Flag, Signal, Event,
    MainFrame, Frame, Box, Orientation, Align,
    Widget, WidgetBase, Button, Label)


class Window(MainFrame):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.signal(Event.MOUSE_RIGHT_BUTTON_PRESS).connect(self.ctx)
        # self.signal(Event.MOUSE_BUTTON_PRESS).connect(self.fn_label)
        # self.signal(Event.TITLE_CHANGE).connect(lambda: print('TITLE_CHANGE'))
        # self.signal(Event.STATE_CHANGE).connect(lambda: print('STATE_CHANGE'))
        # self.signal(Event.FOCUS_IN).connect(lambda: print('FOCUS_IN'))
        # self.signal(Event.FOCUS_OUT).connect(lambda: print('FOCUS_OUT'))

        self.align = Align.TOP
        self.button = self.insert(Button('Button'))
        self.button.signal(Event.MOUSE_BUTTON_PRESS).connect(
            lambda: print(self.button.text))

        self.block_button = self.insert(Button('Block Button'))
        self.block_button.signal(Event.MOUSE_BUTTON_PRESS).connect(
            self.on_block_button)

        self.btn = self.insert(Button('Last Button'))
        self.btn.signal(Event.MOUSE_BUTTON_PRESS).connect(lambda: print('x'))

        self.ctx_menu = Frame()
        self.cursor = Cursor()

        # self.style_from_file('stylerc')
        # pprint.pprint(self.style['[Button]'])

    def ctx(self):
        self.ctx_menu.flag = Flag.POPUP
        self.ctx_menu.show()
        self.ctx_menu.move(self.cursor.x() - 5, self.cursor.y() - 5)

    def on_block_button(self):
        if self.button.enabled:
            self.button.enabled = False
            self.block_button.text = 'Unblock Button'
            self.btn.style_class = 'Warning'
        else:
            self.button.enabled = True
            self.block_button.text = 'Block Button'
            self.btn.style_class = None


if __name__ == '__main__':
    # from PySide6 import QtCore, QtGui, QtWidgets
    # from __feature__ import snake_case
    # import cells.core.coreshadow as shadow

    app = Application(sys.argv)

    # s = shadow.CoreMainFrameShadow()
    # s.set_window_flags(
    #     QtCore.Qt.FramelessWindowHint | QtCore.Qt.Window)

    app.frame = Window()
    app.frame_id = [__file__, 'my_app', 'My App']
    app.icon = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'icon.svg')
    app.exec()
