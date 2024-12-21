#!/usr/bin/env python3
import os
import sys
import pprint

from cells import (
    Application, MainFrame, Flag, Frame, Signal, Event, Cursor, Box, Label,
    Widget)


class Wid(Widget):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.style_id = 'Wid'
        self.style['[Wid]']['background'] = 'rgba(0, 200, 0, 0.30)'
        self.style = self.style


class Window(MainFrame):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        # self.event_signal(Event.MOUSE_BUTTON_PRESS).connect(self.fn_label)

        self.event_signal(Event.MOUSE_RIGHT_BUTTON_PRESS).connect(self.ctx)

        # self.event_signal(Event.TITLE_CHANGE).connect(
        #     lambda: print('TITLE_CHANGE'))

        # self.event_signal(Event.STATE_CHANGE).connect(
        #     lambda: print('STATE_CHANGE'))

        # self.event_signal(Event.FOCUS_IN).connect(
        #     lambda: print('FOCUS_IN'))

        # self.event_signal(Event.FOCUS_OUT).connect(
        #     lambda: print('FOCUS_OUT'))
        self.box = self.add_box()
        self.label = self.box.add_widget(Label('hello'))
        self.label_count = 0
        self.event_signal(Event.MOUSE_BUTTON_PRESS).connect(self.fn_label)

        self.new_box = self.box.add_box()

        self.wid = self.new_box.add_widget(Wid(is_base=False))
        self.wid.margin = 30, 15, 15, 15

        self.w = None
        for n in range(5):
            w = self.box.add_widget(Widget(is_base=False))
            if n == 3:
                w.style_id = f'Wid{n}'
                w.style[f'[Wid{n}]']['background'], w.style = 'rgba(200, 0, 0, 1.00)', w.style
                self.w = w

        self.w.style['[Wid3]']['background'] = 'rgba(0, 0, 200, 0.30)'
        self.w.style = self.w.style

        self.ctx_menu = Frame()
        self.cursor = Cursor()

    def fn_label(self):
        self.label_count += 1
        self.label.text = f'Clicked: {self.label_count}'

    def ctx(self):
        self.ctx_menu.flags = [Flag.POPUP]
        self.ctx_menu.show()
        self.ctx_menu.move(self.cursor.x() - 5, self.cursor.y() - 5)


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
