#!/usr/bin/env python3
import os
# os.environ["QT_QPA_PLATFORM"] = "xcb"

import sys
import pprint

from cells import (
    Application, Cursor, Flag, Signal, Event,
    MainFrame, Frame, MoveFrame, Box, Orientation, Align,
    Widget, Button, ToolButton, Label, Image, Icon, RadioButton, RadioGroup,
    CheckButton)


class MyApp(MainFrame):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        # self.signal(Event.MOUSE_PRESS).connect(self.fn_label)
        # self.signal(Event.TITLE).connect(lambda: print('TITLE_CHANGE'))
        # self.signal(Event.STATE).connect(lambda: print('STATE_CHANGE'))
        # self.signal(Event.FOCUS_IN).connect(lambda: print('FOCUS_IN'))
        # self.signal(Event.FOCUS_OUT).connect(lambda: print('FOCUS_OUT'))
        self.spacing = 5
        self.move_frame = self.insert(MoveFrame())

        # self.radio_1 = self.insert(RadioButton('Radio 1'))
        # self.radio_2 = self.insert(RadioButton('Radio 2', True))
        self.radio_group = self.insert(RadioGroup([
            RadioButton('Radio 1', 'radio1'),
            RadioButton('Radio 2', 'radio2', True)]))

        self.check_1 = self.insert(CheckButton('Check 1'))
        self.check_2 = self.insert(CheckButton('Check 2', True))
        
        self.button_t = self.insert(ToolButton('document-open'))
        self.button_t.selectable = True
        self.button = self.insert(Button('Button text', 'document-open'))
        self.button.selectable = True
        self.button.signal(Event.MOUSE_PRESS).connect(
            lambda: print(self.button.text))

        self.block_button = self.insert(Button('Block Button'))
        self.block_button.signal(Event.MOUSE_PRESS).connect(
            self.on_block_button)

        # self.btn = self.insert(Button('Button'))
        # self.btn.signal(Event.MOUSE_PRESS).connect(lambda: print('Widget: MOUSE_PRESS'))
        # self.btn.signal(Event.MOUSE_RELEASE).connect(lambda: print('Widget: MOUSE_RELEASE'))
        # self.btn.signal(Event.MOUSE_DOUBLE_PRESS).connect(lambda: print('Widget: MOUSE_DOUBLE_PRESS'))
        # self.btn.signal(Event.MOUSE_HOVER_ENTER).connect(lambda: print('Widget: MOUSE_HOVER_ENTER'))
        # self.btn.signal(Event.MOUSE_HOVER_LEAVE).connect(lambda: print('Widget: MOUSE_HOVER_LEAVE'))
        # self.btn.signal(Event.MOUSE_HOVER_MOVE).connect(lambda: print('Widget: MOUSE_HOVER_MOVE'))
        # self.btn.signal(Event.MOUSE_RIGHT_PRESS).connect(lambda: print('Widget: MOUSE_RIGHT_BUTTON_PRESS'))
        # self.btn.signal(Event.MOUSE_WHEEL).connect(lambda: print('Widget: MOUSE_WHEEL'))
        # self.btn.signal(Event.INSERT).connect(lambda: print('Widget: INSERT'))
        # self.btn.signal(Event.REMOVE).connect(lambda: print('Widget: REMOVE'))
        # self.btn.signal(Event.DELETE).connect(lambda: print('Widget: DELETE'))
        # self.btn.signal(Event.SIZE).connect(lambda: print('Widget: SIZE'))
        # self.btn.signal(Event.STYLE).connect(lambda: print('Widget: STYLE'))
        # self.btn.signal(Event.STYLE_ID).connect(lambda: print('Widget: STYLE_ID'))
        # self.btn.signal(Event.ENABLED).connect(lambda: print('Widget: ENABLED'))
        # self.btn.signal(Event.MAIN_PARENT).connect(lambda: print('Widget: MAIN_PARENT'))
        # self.btn.signal(Event.STYLE_CLASS).connect(lambda: print('Widget: STYLE_CLASS'))

        self.ctx_menu = Frame()
        self.cursor = Cursor()
        self.signal(Event.MOUSE_RIGHT_PRESS).connect(self.ctx)

        img = self.insert(Image(Icon('document-open')))
        img.style_class = 'Success'
        img.style_id = 'NewImage'
        img.style['[NewImage]']['border'] = '1px rgba(0, 0, 0, 0.00)'
        img.style = img.style

        self.btnx = self.insert(Button('Radio value'))
        self.btnx.signal(Event.MOUSE_PRESS).connect(lambda: print(self.radio_group.value()))

        # self.style_from_file('stylerc')

    def ctx(self):
        self.ctx_menu.flag = Flag.POPUP
        self.ctx_menu.show()
        self.ctx_menu.move(self.cursor.x() - 5, self.cursor.y() - 5)

    def on_block_button(self):
        if self.button.enabled:
            self.button.enabled = False
            # self.radio_1.selected = True
            self.check_1.selected = True
            self.check_1.style_class = 'Danger'
            self.btnx.selected = True
        else:
            self.button.enabled = True
            self.button.state = None
            # self.radio_1.selected = False
            self.check_1.selected = False
            self.check_1.style_class = None
            self.btnx.selected = False


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
