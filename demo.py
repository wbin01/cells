#!/usr/bin/env python3
import os
import sys

from cells import Application, MainFrame, Frame, Signal, Event


class MainFrame(MainFrame):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.event_signal(Event.FOCUS_IN).callback(
            lambda: print('FOCUS_IN'))
        self.event_signal(Event.FOCUS_OUT).callback(
            lambda: print('FOCUS_OUT'))
        self.event_signal(Event.HOVER_ENTER).callback(
            lambda: print('HOVER_ENTER'))
        self.event_signal(Event.HOVER_LEAVE).callback(
            lambda: print('HOVER_LEAVE'))
        # self.event_signal(Event.HOVER_MOVE).callback(
        #     lambda: print('HOVER_MOVE'))
        self.event_signal(Event.MOUSE_CLICK).callback(
            lambda: print('MOUSE_CLICK'))
        self.event_signal(Event.MOUSE_DOUBLE_CLICK).callback(
            lambda: print('MOUSE_DOUBLE_CLICK'))
        self.event_signal(Event.MOUSE_RIGHT_CLICK).callback(
            lambda: print('MOUSE_RIGHT_CLICK'))
        self.event_signal(Event.MOUSE_WHEEL).callback(
            lambda: print('MOUSE_WHEEL'))


if __name__ == '__main__':
    app = Application(sys.argv)
    app.frame = MainFrame()
    app.frame_id = [__file__, 'cells', 'Cells']
    app.icon = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'icon.svg')
    app.exec()
