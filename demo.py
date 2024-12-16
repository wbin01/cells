#!/usr/bin/env python3
import os
import sys
import pprint

from cells import (
    Application, MainFrame, Frame, Signal, Event, Cursor, Box, Label, Button, Widget)


class MainFrame(MainFrame):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        # self.event_signal(Event.MOUSE_BUTTON_PRESS).connect(
        #     lambda: self.fun('Hello', 'World'))

        # self.event_signal(Event.MOUSE_RIGHT_BUTTON_PRESS).connect(self.xxx)

        # self.event_signal(Event.TITLE_CHANGE).connect(
        #     lambda: print('TITLE_CHANGE'))

        # self.event_signal(Event.STATE_CHANGE).connect(
        #     lambda: print('STATE_CHANGE'))

        # self.event_signal(Event.FOCUS_IN).connect(
        #     lambda: print('FOCUS_IN'))

        # self.event_signal(Event.FOCUS_OUT).connect(
        #     lambda: print('FOCUS_OUT'))

        # self.box = Box()
        # self.add_box(self.box)
        self.box = self.add_box(Box())

        self.top = None

        for n in range(10):
            # w = Widget()
            # self.box.add_widget(w)
            w = self.box.add_widget(Widget())
            
            if n == 3:
                w.style_id = f'Wid{n}'
                w.style[f'[Wid{n}]']['background'] = 'rgba(200, 0, 0, 1.00)'
                w.style = w.style

                self.top = w

        self.top.style[f'[Wid3]']['background'] = 'rgba(0, 0, 200, 1.00)'
        self.top.style = self.top.style

        for n in range(10):
            _, w = setattr(self, 'w' + str(n), Widget()), getattr(self, 'w' + str(n))
            self.box.add_widget(w)

        self.wid = getattr(self, 'w' + str(3))
        self.wid.style_id = 'Widg3'
        self.wid.style[f'[Widg3]']['background'] = 'rgba(0, 200, 0, 1.00)'
        self.wid.style = self.wid.style

        self.num = 0

    def btn_fun(self, args):
        self.num += 1
        self.label.text = f'Button Clicked: {self.num}'


if __name__ == '__main__':
    # from PySide6 import QtCore, QtGui, QtWidgets
    # from __feature__ import snake_case
    # import cells.core.coreshadow as shadow

    app = Application(sys.argv)

    # s = shadow.CoreMainFrameShadow()
    # s.set_window_flags(
    #     QtCore.Qt.FramelessWindowHint | QtCore.Qt.Window)

    app.frame = MainFrame()
    app.frame_id = [__file__, 'my_app', 'My App']
    app.icon = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'icon.svg')
    app.exec()
