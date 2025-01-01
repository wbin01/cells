#!/usr/bin/env python3
import os

from PySide6 import QtGui
from __feature__ import snake_case


class Icon(object):
    """Icon."""
    def __init__(
            self,
            path: str = None,
            fallback_path: str = None,
            width: int = 22,
            height: int = 22,
            *args, **kwargs) -> None:
        """Class constructor.

        The icon is rendered from the path of a passed file, or from the name 
        of an icon in the current operating system, such as "folder-download". 
        To find out all the system icon names, see the "freedesktop.org" 
        specification:
            https://specifications.freedesktop.org/icon-naming-spec/latest/

        Although the Freedesk specification is for Linux, we are making it 
        compatible with Windows (Aesthetically compatible alternative icons). 
        If an icon is not found, it will not give an error, but it will also 
        not render any image, so to ensure an image is rendered use a file 
        path as a fallback (fallback_path).

        :param path: Icon path or icon name from system, like "folder-download"
        :param fallback_path: fallback icon path.
        :param width: Integer with the value of the icon width. Default is 22
        :param height: Integer with the value of the icon height. Default is 22
        """
        super().__init__(*args, **kwargs)
        self.__path = path
        self.__fallback_path = fallback_path if fallback_path else ''
        self.__width = width
        self.__height = height

        if not os.path.isfile(self.__path):
            # TODO: Not Linux alternative here ...
            self.__icon = QtGui.QIcon.from_theme(self.__path)

            if not self.__icon.has_theme_icon(self.__path):
                self.__icon = QtGui.QIcon(self.__fallback_path)
                self.__icon.pixmap(self.__width, self.__height)
            else:
                self.__icon.pixmap(self.__width, self.__height)
        else:
            self.__icon = QtGui.QIcon(self.__path)
            self.__icon.pixmap(self.__width, self.__height)

    @property
    def height(self) -> int:
        """Returns the height of the Icon.

        Pass a new integer value to update the height.
        """
        return self.__height

    @height.setter
    def height(self, height) -> None:
        self.__height = height
        self.__icon.pixmap(self.__width, self.__height)

    @property
    def path(self) -> str:
        """Icon path.

        Pass a new path to update the icon image.
        """
        return self.__path

    @path.setter
    def path(self, path: str) -> None:
        self.__path = path
        self.__icon = QtGui.QIcon(self.__path)
        # self.__icon.add_pixmap(path)

    @property
    def width(self) -> int:
        """Returns the Widget width.

        Pass a new integer value to update the width.
        """
        return self.__width

    @width.setter
    def width(self, width) -> None:
        self.__width = width
        self.__icon.pixmap(self.__width, self.__height)

    @property
    def _obj(self):
        """Direct access to Qt classes.

        Warning: Direct access is discouraged and may break the project. 
        This access is considered a hacking for complex Qt implementations, 
        and should only be used for testing and analysis purposes.
        """
        return self.__icon

    @_obj.setter
    def _obj(self, obj: QtGui) -> None:
        self.__icon = obj

    def __str__(self):
        return f'<Icon: {id(self)}>'
