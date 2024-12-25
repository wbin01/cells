#!/usr/bin/env python3
import os
import sys
import pprint

from cells import (
    Application, Cursor, Flag, Signal, Event,
    MainFrame, Frame, Box, Orientation, Align,
    Widget, WidgetBase, Label)


class Wid(Widget):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.style_id = 'Wid'
        self.style['[Wid]']['background'] = 'rgba(0, 200, 0, 0.30)'
        self.style = self.style


class Window(MainFrame):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.signal(Event.MOUSE_RIGHT_BUTTON_PRESS).connect(self.ctx)
        # self.signal(Event.MOUSE_BUTTON_PRESS).connect(self.fn_label)
        # self.signal(Event.TITLE_CHANGE).connect(lambda: print('TITLE_CHANGE'))
        # self.signal(Event.STATE_CHANGE).connect(lambda: print('STATE_CHANGE'))
        # self.signal(Event.FOCUS_IN).connect(lambda: print('FOCUS_IN'))
        # self.signal(Event.FOCUS_OUT).connect(lambda: print('FOCUS_OUT'))

        self.top_label = self.insert(Label('Insert Label'))
        self.top_label.style_id = 'TopLabel'
        self.top_label.style['[TopLabel]']['background'] = 'rgba(200, 0, 0, 1.00)'
        self.top_label.style['[TopLabel:hover]']['background'] = 'rgba(200, 0, 200, 1.00)'
        self.top_label.style = self.top_label.style

        self.box = self.insert(Box())
        self.box.align = Align.LEFT
        self.box.spacing = 5
        self.box.margin = 0, 0, 0, 10
        # self.box.signal(Event.INSERT_ITEM).connect(lambda: print('INSERT'))
        # self.box.signal(Event.REMOVE_ITEM).connect(lambda: print('REMOVE'))

        self.label = self.box.insert(Label('hello'))
        self.label_count = 0
        self.signal(Event.MOUSE_BUTTON_PRESS).connect(self.fn_label)

        self.new_box = self.box.insert(Box())

        self.wid = self.new_box.insert(Wid(orientation=Orientation.HORIZONTAL))
        self.label_2 = self.wid.insert(Label('l1'))
        self.label_2.style['[Label]']['background'] = 'rgba(200, 0, 200, 1.00)'
        self.label_2.style = self.label_2.style
        self.label_2.text = 'l+'

        self.label_3 = self.wid.insert(Label('l2'))

        self.w = None
        for n in range(5):
            w = self.box.insert(WidgetBase())
            w.minimum_height = 20
            if n == 3:
                w.style_id = 'Wid3'
                w.style['[Wid3]']['background'], w.style = 'rgba(200, 0, 0, 1.00)', w.style
                self.w = w

        self.w.style['[Wid3]']['background'] = 'rgba(0, 0, 200, 0.30)'
        self.w.style['[Wid3:hover]']['background'] = 'rgba(200, 0, 200, 1.00)'
        self.w.style = self.w.style

        self.ctx_menu = Frame()
        self.cursor = Cursor()

    def fn_label(self):
        self.label_count += 1
        self.label.text = f'Clicked: {self.label_count}'

    def ctx(self):
        self.ctx_menu.flags = [Flag.POPUP]
        self.ctx_menu.show()
        self.ctx_menu.move(self.cursor.x() - 5, self.cursor.y() - 5)


if __name__ == '__main__':
    # from PySide6 import QtCore, QtGui, QtWidgets
    # from __feature__ import snake_case
    # import cells.core.coreshadow as shadow

    app = Application(sys.argv)

    # s = shadow.CoreMainFrameShadow()
    # s.set_window_flags(
    #     QtCore.Qt.FramelessWindowHint | QtCore.Qt.Window)

    app.frame = Window()
    app.frame_id = [__file__, 'my_app', 'My App']
    app.icon = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'icon.svg')
    app.exec()
