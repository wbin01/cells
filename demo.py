#!/usr/bin/env python3
import os
import sys

from cells import Application, MainFrame, Frame, Signal


class MainFrame(MainFrame):
    def __init__(self, *args, **kwargs) -> None:
        """Class constructor"""
        super().__init__(*args, **kwargs)
        self.signal('mouse-left-click').callback(self.bg_style)
        self.print_style()

    def print_style(self):
        for key, value in self.style.items():
            print(f'\n{key}')
            for k, v in value.items():
                print(k, '=', v)

    def bg_style(self):
        ss = self.style
        ss['[MainFrame]']['background'] = 'rgba(255, 0, 0, 1.00)'
        self.style = ss
        print('--')
        self.print_style()


if __name__ == '__main__':
    app = Application(sys.argv)
    app.frame = MainFrame()
    app.frame_id = [__file__, 'cells', 'Cells']
    app.icon = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'icon.svg')
    app.exec()
