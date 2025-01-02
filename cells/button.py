#!/usr/bin/env python3
from .align import Align
from .box import Box
from .event import Event
from .icon import Icon
from .image import Image
from .label import Label
from .orientation import Orientation
from .widget import Widget


class Button(Widget):
    """Button Widget."""
    def __init__(
            self,
            text: str = None,
            icon: str = None,
            *args, **kwargs) -> None:
        """Class constructor."""
        super().__init__(*args, **kwargs)
        self.__text = text if text else ''
        self.__icon = Icon(icon) if icon else icon
        self.style_id = 'Button'
        self.__focus = True
        self.__icon_on_right = False
        self.__tool = True

        self.__base_box = self.insert(Box(orientation=Orientation.HORIZONTAL))
        self.__base_box.spacing = 2
        self.__base_box.margin = 0, 5, 0, 5
        self.__base_box.align = Align.CENTER

        if self.__icon and not self.__icon_on_right:
            self.__icon = self.__base_box.insert(Image(self.__icon))
        
        self.__label = Label(self.__text)
        if self.__text:
            self.__base_box.insert(self.__label)

        if self.__icon and self.__icon_on_right:
            self.__icon = self.__base_box.insert(Image(self.__icon))

        self.signal(Event.MAIN_PARENT).connect(self.__on_main_added)
        self.signal(Event.ENABLED).connect(self.__on_enabled_change)
        self.signal(Event.STYLE_CLASS).connect(self.style_id_tool)

        self.signal(Event.MOUSE_HOVER_ENTER).connect(
            self.__on_mouse_hover_enter)
        self.signal(Event.MOUSE_HOVER_LEAVE).connect(
            self.__on_mouse_hover_leave)
        self.signal(Event.MOUSE_BUTTON_PRESS).connect(
            self.__on_mouse_button_press)
        self.signal(Event.MOUSE_BUTTON_RELEASE).connect(
            self.__on_mouse_button_release)

    def style_id_tool(self):
        if self.style_class == 'ToolButton':
            self.__label.visible = False
            self.__base_box.margin = 0, 0, 0, 0
            self.height = self.__icon.height + 10
            self.width = self.__icon.width + 10

    @property
    def text(self) -> str:
        """Button text.
        
        Pass a new string to update the text.
        """
        return self.__label.text

    @text.setter
    def text(self, text: str) -> None:
        self.__text = text
        self.__label.text = text

    def __on_enabled_change(self) -> None:
        if self.enabled:
            self.__on_main_parent_focus_in()
        else:
            self.__on_main_parent_focus_out()

        if self.__icon:
            self.__icon.enabled = self.enabled

    def __on_main_added(self) -> None:
        self._main_parent.signal(Event.FOCUS_IN).connect(
            self.__on_main_parent_focus_in)
        self._main_parent.signal(Event.FOCUS_OUT).connect(
            self.__on_main_parent_focus_out)
        
        if self.__icon:
            self.__icon._main_parent = self._main_parent

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
