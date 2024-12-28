#!/usr/bin/env python3
from PySide6 import QtWidgets, QtGui, QtCore
from __feature__ import snake_case

from .align import Align
from .event import Event
from .label import Label
from .orientation import Orientation
from .widget import Widget
from .box import Box


class Button(Widget):
    """Button Widget."""
    def __init__(self, text: str = '', *args, **kwargs) -> None:
        """Class constructor."""
        super().__init__(*args, **kwargs)
        self.style_id = 'Button'
        self.__focus = True
        self.__default = False
        self.__saved_style = None
        self.__shadow = QtWidgets.QGraphicsDropShadowEffect()

        self.__base_box = self.insert(Box(orientation=Orientation.HORIZONTAL))
        self.__base_box.align = Align.CENTER
        self.__label =  self.__base_box.insert(Label(text))
        self.__label.margin = 0, 5, 0, 5
        
        self.signal(Event.MAIN_PARENT_ADDED).connect(self.__on_main_added)
        self.signal(Event.ENABLED_CHANGE).connect(self.__on_enabled_change)

        self.signal(Event.MOUSE_HOVER_ENTER).connect(
            self.__on_mouse_hover_enter)
        self.signal(Event.MOUSE_HOVER_LEAVE).connect(
            self.__on_mouse_hover_leave)
        self.signal(Event.MOUSE_BUTTON_PRESS).connect(
            self.__on_mouse_button_press)
        self.signal(Event.MOUSE_BUTTON_RELEASE).connect(
            self.__on_mouse_button_release)

    @property
    def default(self) -> bool:
        """..."""
        return self.__default

    @default.setter
    def default(self, value: str) -> None:
        self.__default = value
        if self._main_parent:
            if not self.__saved_style:
                style = {
                    f'[{self.style_id}]': self._main_parent.style[
                        f'[{self.style_id}]'],
                    f'[{self.style_id}:hover]': self._main_parent.style[
                        f'[{self.style_id}:hover]'],
                    f'[{self.style_id}:pressed]': self._main_parent.style[
                        f'[{self.style_id}:pressed]'],
                    f'[{self.style_id}:inactive]': self._main_parent.style[
                        f'[{self.style_id}:inactive]']}
                self.__saved_style = style

            if self.__default:
                rgb = [int(x) for x in self.accent]
                self.__shadow = QtWidgets.QGraphicsDropShadowEffect()
                self.__shadow.set_blur_radius(5)
                self.__shadow.set_offset(0, 0)
                self.__shadow.set_color(QtGui.QColor(rgb[0], rgb[1], rgb[2]))
                self._obj.set_graphics_effect(self.__shadow)

                self.style = {
                    f'[{self.style_id}]': self._main_parent.style[
                        '[Button-Default]'],
                    f'[{self.style_id}:hover]': self._main_parent.style[
                        '[Button-Default:hover]'],
                    f'[{self.style_id}:pressed]': self._main_parent.style[
                        '[Button-Default:pressed]'],
                    f'[{self.style_id}:inactive]': self._main_parent.style[
                        '[Button-Default:inactive]']}
            else:
                if self.__saved_style:
                    self._obj.set_graphics_effect(None)
                    self.style = self.__saved_style
                    self.__saved_style = None

    @property
    def text(self) -> str:
        """Button text.
        
        Pass a new string to update the text.
        """
        return self.__label.text

    @text.setter
    def text(self, text: str) -> None:
        self.__label.text = text

    def __on_enabled_change(self) -> None:
        if self.enabled:
            self.__on_main_parent_focus_in()
        else:
            self.__on_main_parent_focus_out()

    def __on_main_added(self) -> None:
        self._main_parent.signal(Event.FOCUS_IN).connect(
            self.__on_main_parent_focus_in)
        self._main_parent.signal(Event.FOCUS_OUT).connect(
            self.__on_main_parent_focus_out)

    def __on_main_parent_focus_in(self) -> None:
        self.__focus = True
        if self.enabled:
            self.__label.style['[Label]']['color'] = self.style[
                f'[{self.style_id}]']['color']
            self.__label.style = self.__label.style

    def __on_main_parent_focus_out(self) -> None:
        self.__focus = False
        self.__label.style['[Label]']['color'] = self.style[
            f'[{self.style_id}:inactive]']['color']
        self.__label.style = self.__label.style

    def __on_mouse_hover_enter(self) -> None:
        if self.enabled and self.__focus:
            self.__label.style['[Label]']['color'] = self.style[
                f'[{self.style_id}:hover]']['color']
            self.__label.style = self.__label.style

    def __on_mouse_hover_leave(self) -> None:
        if self.enabled and self.__focus:
            self.__label.style['[Label]']['color'] = self.style[
                f'[{self.style_id}]']['color']
            self.__label.style = self.__label.style

    def __on_mouse_button_press(self) -> None:
        if self.enabled and self.__focus:
            self.__label.style['[Label]']['color'] = self.style[
                f'[{self.style_id}:pressed]']['color']
            self.__label.style = self.__label.style

    def __on_mouse_button_release(self) -> None:
        if self.enabled and self.__focus:
            self.__label.style['[Label]']['color'] = self.style[
                f'[{self.style_id}:hover]']['color']
            self.__label.style = self.__label.style

    def __str__(self) -> str:
        return f'<Button: {id(self)}>'

# setShortcut(QKeySequence(Qt::Key_Enter))
# setShortcut(QKeySequence(Qt::Key_Enter));
# setShortcut(QKeySequence::StandardKey::)

# QKeySequence(QKeySequence.Print)
# QKeySequence(tr("Ctrl+P"))
# QKeySequence(tr("Ctrl+p"))

# https://doc.qt.io/qtforpython-6/PySide6/
# QtGui/QKeySequence.html#PySide6.QtGui.QKeySequence

# https://doc.qt.io/qtforpython-6/PySide6/QtGui/
# QKeySequence.html#PySide6.QtGui.QKeySequence.StandardKey


# self._obj.set_shortcut(QtGui.QKeySequence('Enter'))
# # QtCore.Qt.Key_Return
# self._obj.set_default(True)
