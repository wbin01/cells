#!/usr/bin/env python3
import os
# os.environ["QT_QPA_PLATFORM"] = "xcb"

import sys
import pprint

from cells import (
    Application, Cursor, Flag, Signal, Event,
    MainFrame, Frame, MoveFrame, Box, Orientation, Align,
    Widget, Button, Label, Image, Icon, RadioButton)


class MyApp(MainFrame):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        # self.signal(Event.MOUSE_PRESS).connect(self.fn_label)
        # self.signal(Event.TITLE).connect(lambda: print('TITLE_CHANGE'))
        # self.signal(Event.STATE).connect(lambda: print('STATE_CHANGE'))
        # self.signal(Event.FOCUS_IN).connect(lambda: print('FOCUS_IN'))
        # self.signal(Event.FOCUS_OUT).connect(lambda: print('FOCUS_OUT'))
        self.spacing = 5
        # self.align = Align.TOP
        self.move_frame = self.insert(MoveFrame())

        self.radio_1 = self.insert(RadioButton('Radio'))
        self.radio_1.signal(Event.MOUSE_PRESS).connect(lambda: print(222))
        # self.radio_1.style_class = 'Warning'
        
        self.button = self.insert(Button('Button text', 'document-open'))
        # self.button.insert(Image(Icon()))
        # self.button.align = Align.LEFT
        # self.button.style_class = 'ToolButton'
        self.button.signal(Event.MOUSE_PRESS).connect(
            lambda: print(self.button.text))

        self.block_button = self.insert(Button('Block Button'))
        self.block_button.signal(Event.MOUSE_PRESS).connect(
            self.on_block_button)

        self.btn = self.insert(Button('Last Button'))
        # self.btn.signal(Event.MOUSE_PRESS).connect(lambda: print('Widget: MOUSE_PRESS'))
        # self.btn.signal(Event.MOUSE_RELEASE).connect(lambda: print('Widget: MOUSE_RELEASE'))
        # self.btn.signal(Event.MOUSE_DOUBLE_PRESS).connect(lambda: print('Widget: MOUSE_DOUBLE_PRESS'))
        # self.btn.signal(Event.MOUSE_HOVER_ENTER).connect(lambda: print('Widget: MOUSE_HOVER_ENTER'))
        # self.btn.signal(Event.MOUSE_HOVER_LEAVE).connect(lambda: print('Widget: MOUSE_HOVER_LEAVE'))
        # self.btn.signal(Event.MOUSE_HOVER_MOVE).connect(lambda: print('Widget: MOUSE_HOVER_MOVE'))
        # self.btn.signal(Event.MOUSE_RIGHT_PRESS).connect(lambda: print('Widget: MOUSE_RIGHT_BUTTON_PRESS'))
        # self.btn.signal(Event.MOUSE_WHEEL).connect(lambda: print('Widget: MOUSE_WHEEL'))
        self.btn.signal(Event.INSERT).connect(lambda: print('Widget: INSERT'))
        self.btn.signal(Event.REMOVE).connect(lambda: print('Widget: REMOVE'))
        self.btn.signal(Event.DELETE).connect(lambda: print('Widget: DELETE'))
        # self.btn.signal(Event.SIZE).connect(lambda: print('Widget: SIZE'))
        # self.btn.signal(Event.STYLE).connect(lambda: print('Widget: STYLE'))
        # self.btn.signal(Event.STYLE_ID).connect(lambda: print('Widget: STYLE_ID'))
        # self.btn.signal(Event.ENABLED).connect(lambda: print('Widget: ENABLED'))
        # self.btn.signal(Event.MAIN_PARENT).connect(lambda: print('Widget: MAIN_PARENT'))
        # self.btn.signal(Event.STYLE_CLASS).connect(lambda: print('Widget: STYLE_CLASS'))

        self.ctx_menu = Frame()
        self.cursor = Cursor()
        self.signal(Event.MOUSE_RIGHT_PRESS).connect(self.ctx)

        for i in range(5):
            self.insert(Label(str(i)))

        self.wid = self.insert(Widget())
        self.wid.height = 30

        self.label = Label('INSERT')
        # self.wid.insert(Label('INSERT_x x'))

        img = self.insert(Image(Icon('document-open')))
        img.style_class = 'Success'
        img.style_id = 'NewImage'
        img.style['[NewImage]']['border'] = '1px rgba(0, 0, 0, 0.00)'
        img.style = img.style

        # self.style_from_file('stylerc')
        self.lbl = self.insert(Label('7777'))

    def ctx(self):
        self.ctx_menu.flag = Flag.POPUP
        self.ctx_menu.show()
        self.ctx_menu.move(self.cursor.x() - 5, self.cursor.y() - 5)

    def on_block_button(self):
        if self.button.enabled:
            self.button.enabled = False
            self.button.state = 'hover'
            self.block_button.text = 'Unblock Button'
            # self.btn.style_id = 'Master'
            # self.btn.style_class = 'Warning'
            self.btn.state = 'hover'

            # self.btn.height = 50
            # self.wid.insert(self.label)
            self.label.style_class = 'Danger'
            self.label.style[
                '[Label]']['border'] = '0px 0px 0px 0px rgba(0, 0, 0, 0.0)'
            self.label.style = self.label.style
            # self.remove(self.btn)

            # self.radio_1.enabled = False
            self.radio_1.state = 'hover'
            # self.radio_1.style_class = 'Danger'
            self.lbl.state = 'inactive'
        else:
            self.lbl.state = None
            self.button.enabled = True
            self.button.state = None
            self.block_button.text = 'Block Button'
            # self.btn.style_class = None
            self.btn.state = None

            # self.btn.height = 20
            self.label.style_class = None
            # self.wid.remove(self.label)
            # self.btn.delete(self.label)
            # self.radio_1.enabled = True
            self.radio_1.state = None
            # self.radio_1.style_class = None


if __name__ == '__main__':
    # from PySide6 import QtCore, QtGui, QtWidgets
    # from __feature__ import snake_case
    # import cells.core.coreshadow as shadow
    
    # from PySide6.QtGui import QGuiApplication
    # print(QGuiApplication.platformName())

    app = Application(sys.argv)

    # s = shadow.CoreMainFrameShadow()
    # s.set_window_flags(
    #     QtCore.Qt.FramelessWindowHint | QtCore.Qt.Window)
    
    app.frame = MyApp()
    app.frame_id = [__file__, 'my_app', 'My App']
    app.icon = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'icon.svg')
    app.exec()
    
