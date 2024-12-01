#!/usr/bin/env python3
import os
import sys

from cells import (
    Application, MainFrame, Frame, Signal, Event, Cursor, Box, Component)


class MainFrame(MainFrame):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.event_signal(Event.MOUSE_BUTTON_PRESS).callback(
            lambda: print(self.title))

        self.event_signal(Event.MOUSE_RIGHT_BUTTON_PRESS).callback(self.xxx)

        self.event_signal(Event.TITLE_CHANGE).callback(
            lambda: print('TITLE_CHANGE'))

        self.event_signal(Event.STATE_CHANGE).callback(
            lambda: print('STATE_CHANGE'))

        self.bb = Box()
        self.add_box(self.bb)

        self.cc = Component()
        self.add_component(self.cc)

    def xxx(self):
        if self.title == 'Myapp':
            self.title = 'XXX'
        else:
            self.title = 'Myapp'


if __name__ == '__main__':
    app = Application(sys.argv)
    app.frame = MainFrame()
    app.frame_id = [__file__, 'cells', 'Cells']
    app.icon = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'icon.svg')
    app.exec()
