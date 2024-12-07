#!/usr/bin/env python3
import os
import sys
import pprint

from cells import (
    Application, MainFrame, Frame, Signal, Event, Cursor, Box, Label, Button)


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

        self.label = Label('Hello world!')
        self.add_widget(self.label)

        self.btn = Button('Click me')
        self.btn.connect(lambda: self.btn_fun(2024))
        self.add_widget(self.btn)

        self.new_btn = Button('Click me')
        self.add_widget(self.new_btn)
        self.new_btn.style_id = 'NewButton'
        
        self.num = 0

    def btn_fun(self, args):
        self.num += 1
        self.label.text = f'Button Clicked: {self.num}'


if __name__ == '__main__':
    app = Application(sys.argv)
    app.frame = MainFrame()
    app.frame_id = [__file__, 'my_app', 'My App']
    app.icon = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'icon.svg')
    app.exec()
