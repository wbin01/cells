#!/usr/bin/env python3
import os
import sys

from cells import (
    Application, MainFrame, Frame, Signal, Event, Cursor, Box, Label, Button)


class MainFrame(MainFrame):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.event_signal(Event.MOUSE_BUTTON_PRESS).connect(
            lambda: self.fun('Hello', 'World'))

        self.event_signal(Event.MOUSE_RIGHT_BUTTON_PRESS).connect(self.xxx)

        self.event_signal(Event.TITLE_CHANGE).connect(
            lambda: print('TITLE_CHANGE'))

        self.event_signal(Event.STATE_CHANGE).connect(
            lambda: print('STATE_CHANGE'))

        self.event_signal(Event.FOCUS_IN).connect(
            lambda: print('FOCUS_IN'))

        self.event_signal(Event.FOCUS_OUT).connect(
            lambda: print('FOCUS_OUT'))

        self.box = Box()
        self.add_box(self.box)

        self.label = Label('Hello world!')
        self.add_component(self.label)

        self.btn = Button('Click me')
        self.btn.connect(lambda: self.bbb(2024))
        self.add_component(self.btn)

    def fun(self, arg1, arg2):
        print(self, arg1, arg2)

    def xxx(self):
        if self.title == 'Myapp':
            self.title = 'Title'
        else:
            self.title = 'Myapp'

    def bbb(self, args):
        if self.label.text == 'Hello world!':
            self.label.text = 'Hi'
        else:
            self.label.text = 'Hello world!'
        print(args)


if __name__ == '__main__':
    app = Application(sys.argv)
    app.frame = MainFrame()
    app.frame_id = [__file__, 'cells', 'Cells']
    app.icon = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'icon.svg')
    app.exec()
