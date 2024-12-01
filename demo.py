#!/usr/bin/env python3
import os
import sys

from cells import Application, MainFrame, Frame, Signal, Event, Cursor


class MainFrame(MainFrame):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        # self.print_events(False)
        self.event_signal(Event.MOUSE_BUTTON_PRESS).callback(
            lambda: print(self.minimum_width))

        self.event_signal(Event.MOUSE_RIGHT_BUTTON_PRESS).callback(
            self.change_size)

    def change_size(self):
        if self.minimum_width >= 500:
            self.minimum_width = 200
        else:
            self.minimum_width = 500

if __name__ == '__main__':
    app = Application(sys.argv)
    app.frame = MainFrame()
    app.frame_id = [__file__, 'cells', 'Cells']
    app.icon = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'icon.svg')
    app.exec()
