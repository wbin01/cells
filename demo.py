#!/usr/bin/env python3
import os
import sys

from cells import Application, MainFrame, Frame, Signal, Event


class MainFrame(MainFrame):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.default_bg = self.style['[MainFrame]']['background']
        self.signal(Event.HOVER_ENTER).callback(lambda: self.bg_style(True))
        self.signal(Event.HOVER_LEAVE).callback(lambda: self.bg_style(False))

    def bg_style(self, red=False):
        if red:
            style = self.style
            style['[MainFrame]']['background'] = 'rgba(255, 0, 0, 1.00)'
            self.style = style
        else:
            style = self.style
            style['[MainFrame]']['background'] = self.default_bg
            self.style = style


if __name__ == '__main__':
    app = Application(sys.argv)
    app.frame = MainFrame()
    app.frame_id = [__file__, 'cells', 'Cells']
    app.icon = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'icon.svg')
    app.exec()
