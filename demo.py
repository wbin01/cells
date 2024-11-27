#!/usr/bin/env python3
import os
import sys

from cells import Application, MainFrame, Frame, Signal


class MainFrame(MainFrame):

    test_signal = Signal(28)

    def __init__(self, *args, **kwargs) -> None:
        """Class constructor"""
        super().__init__(*args, **kwargs)
        self.events_signal.callback(self.my_func)
        self.test_signal.callback(lambda: print(type(self.test_signal.obj)))

    def my_func(self):
        print(self.events_signal)
        self.test_signal.send()


if __name__ == '__main__':
    app = Application(sys.argv)
    app.frame = MainFrame()
    app.frame_id = [__file__, 'cells', 'Cells']
    app.icon = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'icon.svg')
    app.exec()
