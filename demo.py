#!/usr/bin/env python3
import os
import sys

from cells import Application, MainFrame, Frame, Signal


class MainFrame(MainFrame):

    x_signal = Signal()

    def __init__(self, *args, **kwargs) -> None:
        """Class constructor"""
        super().__init__(*args, **kwargs)
        self.event_filter_signal.callback(self.my_func)
        self.x_signal.callback(lambda: print('zzz'))


    def my_func(self):
        print(self.event_filter_signal)
        print('Hi!')
        self.x_signal.send_signal()


if __name__ == '__main__':
    app = Application(sys.argv)
    app.frame = MainFrame()
    app.frame_id = [__file__, 'cells', 'Cells']
    app.icon = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'icon.svg')
    app.exec()
