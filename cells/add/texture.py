#!/usr/bin/env python3
import pyscreenshot as ImageGrab
from PIL import Image, ImageFilter, ImageEnhance

from PySide6 import QtCore
from __feature__ import snake_case

from ..event import Event


class DiffuseBlur(object):
    """MainFrame Diffuse Blur background."""
    def __init__(self, main_parent, move_frame: None, *args, **kwargs) -> None:
        """Class constructor.
        
        The DiffuseBlur updates the Frame's background whenever the Frame 
        gains focus or whenever the MoveFrame Widget is released.

        :param main_parent: MainFrame application.
        :param move_frame: MoveFrame Widget.
        """
        super().__init__(*args, **kwargs)
        self.__main_parent = main_parent
        self.__move_frame = move_frame

        self.__move_frame.signal(Event.MOUSE_BUTTON_RELEASE).connect(
            lambda: self.__add_texture_thread())
        self.__main_parent.signal(Event.FOCUS_IN).connect(
            lambda: self.__add_texture_thread())

        self.__thread_manager = QtCore.QThreadPool()
        # self.__timer = QtCore.QTimer()
        # self.__timer.set_interval(2000)
        # self.__timer.timeout.connect(self.__add_texture_thread)
        # self.__timer.start()

    def __add_texture(self) -> None:
        if (not self.__main_parent.fullscreen and
            not self.__main_parent.maximized and
            not self.__main_parent.minimized):
            try:
                im = ImageGrab.grab()
                im = im.convert("RGB")
                im_blur = im.filter(ImageFilter.GaussianBlur(radius=50))
                realce = Image.new("RGB", im.size, (32, 32, 32))
                # realce = ImageEnhance.Brightness(realce).enhance(0.9)
                im = Image.blend(im_blur, realce, alpha=0.85)

                im.save("/tmp/screen.png")
                self.__main_parent.style[
                    '[MainFrame]']['background_image'] = '/tmp/screen.png'
                self.__main_parent.style = self.__main_parent.style
            except Exception as e:
                print(e)
        

    def __add_texture_thread(self):
        self.__thread_manager.start(self.__add_texture)
