#!/usr/bin/env python3
import os
import sys

from cells import Application, MainFrame, Frame, Signal, Event, Cursor


class MainFrame(MainFrame):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        # self.print_events(False)
        self.event_signal(Event.MOUSE_BUTTON_PRESS).callback(
            lambda: print(self.is_minimized))

        self.event_signal(Event.MOUSE_RIGHT_BUTTON_PRESS).callback(self.xxx)

        self.event_signal(Event.FRAME_STATE_CHANGE).callback(self.yyy)

    def xxx(self):
        if self.is_minimized:
            self.is_minimized = False
        else:
            self.is_minimized = True

    def yyy(self):
        if self.is_minimized:
            print('min')
        elif self.is_maximized:
            print('max')
        elif self.is_fullscreen:
            print('full')
        else:
            print('normal')

    def print_events(self, mouse_move = False):
        self.event_signal(Event.FOCUS_IN).callback(
            lambda: print('FOCUS_IN'))
        self.event_signal(Event.FOCUS_OUT).callback(
            lambda: print('FOCUS_OUT'))

        self.event_signal(Event.MOUSE_HOVER_ENTER).callback(
            lambda: print('MOUSE_HOVER_ENTER'))
        self.event_signal(Event.MOUSE_HOVER_LEAVE).callback(
            lambda: print('MOUSE_HOVER_LEAVE'))

        if mouse_move:
            self.event_signal(Event.MOUSE_HOVER_MOVE).callback(
                lambda: print(Cursor().position()))

        self.event_signal(Event.MOUSE_BUTTON_PRESS).callback(
            lambda: print('MOUSE_BUTTON_PRESS'))
        self.event_signal(Event.MOUSE_BUTTON_RELEASE).callback(
            lambda: print('MOUSE_BUTTON_RELEASE'))
        self.event_signal(Event.MOUSE_DOUBLE_CLICK).callback(
            lambda: print('MOUSE_DOUBLE_CLICK'))

        self.event_signal(Event.MOUSE_RIGHT_BUTTON_PRESS).callback(
            lambda: print('MOUSE_RIGHT_BUTTON_PRESS'))
        self.event_signal(Event.MOUSE_WHEEL).callback(
            lambda: print('MOUSE_WHEEL'))

        self.event_signal(Event.RESIZE).callback(
            lambda: print('RESIZE'))
        self.event_signal(Event.FRAME_STATE_CHANGE).callback(
            lambda: print('FRAME_STATE_CHANGE'))
        self.event_signal(Event.CLOSE).callback(
            lambda: print('CLOSE'))


if __name__ == '__main__':
    app = Application(sys.argv)
    app.frame = MainFrame()
    app.frame_id = [__file__, 'cells', 'Cells']
    app.icon = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'icon.svg')
    app.exec()
