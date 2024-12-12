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

        self.box = Box()
        self.add_box(self.box)

        # self.ww = Widget()
        # self.box.add_widget(self.ww)

        # self.w = Widget()
        # self.box.add_widget(self.w)
        # self.w.style_id = 'Wid1'
        # self.w.style['[Widget.Wid1]']['background'] = 'rgba(0, 0, 0, 1.00)'
        # self.w.style = self.w.style

        # self.w2 = Widget()
        # self.box.add_widget(self.w2)
        # # self.w2.style_id = 'Wid2'
        # # sss = self.w2.style.copy()
        # # sss['[Widget.Wid2]']['background'] = 'rgba(0, 0, 0, 0.30)'
        # # self.w2.style = sss


        # self.label = Label('Hello world!')
        # self.add_widget(self.label)

        # self.btn = Button('Click me')
        # self.add_widget(self.btn)
        # self.btn.style_id = 'NewBtn'
        # self.btn.connect(lambda: self.btn_fun(2024))
        

        # self.new_btn = Button('Click me')
        # self.add_widget(self.new_btn)
        # self.new_btn.style_id = 'NewButton'
        # # self.new_btn.style['[Button.NewButton]']['background'] = 'rgba(125, 0, 125, 0.30)'
        # # self.new_btn.style = self.new_btn.style

        # self.new_btn2 = Button('Click me')
        # self.add_widget(self.new_btn2)
        # self.new_btn2.style_id = 'NewButton2'
        # # self.new_btn2.style['[Button.NewButton2]']['background'] = 'rgba(0, 0, 125, 0.30)'
        # # self.new_btn2.style = self.new_btn2.style

        self.num = 0
        # pprint.pprint(self.style)


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
