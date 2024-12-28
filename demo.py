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
        self.insert(Label('Zeta 1'))

        self.ll = self.insert(Label('Zeta 2'))
        self.ll.style_id = 'Zeta2'
        self.ll.style['[Zeta2]']['color'] = 'rgba(0, 200, 0, 1.00)'
        self.ll.style = self.ll.style

        self.ooo = self.insert(Label('Zeta 3'))

        self.top_wid = self.insert(Widget())
        self.top_wid.height = 15

        self.my_button = self.insert(Button('My Button'))
        self.my_button.signal(Event.MOUSE_BUTTON_PRESS).connect(
            lambda: print(self.my_button.text))
        self.my_button.margin = 5, 5, 5, 5

        self.block_my_button = self.insert(Button('Block My Button'))
        self.block_my_button.signal(Event.MOUSE_BUTTON_PRESS).connect(
            self.on_block_my_button)
        self.block_my_button.margin = 5, 5, 5, 5

        self.insert(Label('222'))

        self.ctx_menu = Frame()
        self.cursor = Cursor()

        # self.style_from_file('stylerc')
        # pprint.pprint(self.style['[Button]'])

    def fn_label(self):
        self.label_count += 1
        self.label.text = f'Clicked: {self.label_count}'

    def ctx(self):
        self.ctx_menu.flag = Flag.POPUP
        self.ctx_menu.show()
        self.ctx_menu.move(self.cursor.x() - 5, self.cursor.y() - 5)

    def on_block_my_button(self):
        if self.my_button.enabled:
            self.my_button.enabled = False
            self.ll.enabled = False
            self.block_my_button.text = 'Unblock My Button'
        else:
            self.my_button.enabled = True
            self.ll.enabled = True
            self.block_my_button.text = 'Block My Button'

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
