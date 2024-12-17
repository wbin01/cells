#!/usr/bin/env python3
import os
import sys
import pprint

from cells import (
    Application, MainFrame, Frame, Signal, Event, Cursor, Box, Label, Button, Widget)


class Wid(Widget):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.style_id = 'Wid'
        self.style['[Wid]']['background'] = 'rgba(0, 200, 0, 0.30)'
        self.style = self.style


class MainFrame(MainFrame):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        # self.event_signal(Event.MOUSE_BUTTON_PRESS).connect(self.fn_label)

        # self.event_signal(Event.MOUSE_RIGHT_BUTTON_PRESS).connect(self.xxx)

        # self.event_signal(Event.TITLE_CHANGE).connect(
        #     lambda: print('TITLE_CHANGE'))

        # self.event_signal(Event.STATE_CHANGE).connect(
        #     lambda: print('STATE_CHANGE'))

        # self.event_signal(Event.FOCUS_IN).connect(
        #     lambda: print('FOCUS_IN'))

        # self.event_signal(Event.FOCUS_OUT).connect(
        #     lambda: print('FOCUS_OUT'))

        self.box = self.add_box(Box())

        self.label = self.box.add_widget(Label('hello'))
        self.label_count = 0
        self.event_signal(Event.MOUSE_BUTTON_PRESS).connect(self.fn_label)

        self.wid = self.box.add_widget(Wid())

        self.w = None
        for n in range(5):
            w = self.box.add_widget(Widget())
            if n == 3:
                w.style_id = f'Wid{n}'
                w.style[f'[Wid{n}]']['background'], w.style = 'rgba(200, 0, 0, 1.00)', w.style
                self.w = w

        self.w.style['[Wid3]']['background'] = 'rgba(0, 0, 200, 0.30)'
        self.w.style = self.w.style

        self.widg = self.box.add_widget(Widget())
        self.widg.style['[Widget]']['background'], self.widg.style = 'rgba(200, 0, 0, 0.30)', self.widg.style

        
        self.style = {
        '[MainFrame-Border]': {
            'border': '1px 1px 1px 1px rgba(50, 50, 100, 0.80)',
            'border_radius': '10px 10px 10px 10px'}}

        # self.style = self.style_from_file('stylerc')


    def fn_label(self):
        self.label_count += 1
        self.label.text = f'Clicked: {self.label_count}'


if __name__ == '__main__':
    # from PySide6 import QtCore, QtGui, QtWidgets
    # from __feature__ import snake_case
    # import cells.core.coreshadow as shadow

    app = Application(sys.argv)

    # s = shadow.CoreMainFrameShadow()
    # s.set_window_flags(
    #     QtCore.Qt.FramelessWindowHint | QtCore.Qt.Window)

    app.frame = Frame()
    app.frame_id = [__file__, 'my_app', 'My App']
    app.icon = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'icon.svg')
    app.exec()
