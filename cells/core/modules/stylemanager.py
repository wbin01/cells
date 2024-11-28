#!/usr/bin/env python3
import os
import pathlib

from .desktopentryparse import DesktopFile
from .stylemanagerparser import StyleManagerParser


class StyleManager(object):
    """Frame style manager"""

    def __init__(self, *args, **kwargs) -> None:
        """Class constructor"""
        super().__init__(*args, **kwargs)
        self.__style_handler = StyleManagerParser()

        self.__path = pathlib.Path(__file__).resolve().parent
        self.__url = os.path.join(self.__path, 'static', 'stylerc')
        
        self.__dict_style = None
        self.__qss_style = None

        self.__style_file = DesktopFile(self.__url)
        self.stylesheet = self.__style_file.content

    @property
    def stylesheet(self) -> dict:
        """Style as dict

        Get the style as a dictionary or submit a new dictionary style to 
        update it
        """
        return self.__dict_style
    
    @stylesheet.setter
    def stylesheet(self, style: dict) -> None:
        self.__dict_style = style
        self.__qss_style = {
            'active': self.__dict_style_to_qss_str(),
            'inactive': self.__dict_style_to_qss_str(True),
            'fullscreen': self.__dict_style_to_qss_str(fullscreen=True)}

    def stylesheets_for_qss(self) -> dict:
        """..."""
        return self.__qss_style

    def __dict_style_to_qss_str(
            self, inactive: bool = False, fullscreen: bool = False) -> str:
        bg = self.__dict_style['[MainFrame]']['background']
        bd = self.__style_handler.border_str_to_list(
            self.__dict_style['[MainFrame]']['border'])
        bdr = self.__style_handler.border_radius_str_to_list(
            self.__dict_style['[MainFrame]']['border radius'])
        pd = self.__style_handler.margin_padding_str_to_list(
            self.__dict_style['[MainFrame]']['padding'])

        if inactive:  # Only colors
            if 'background' in self.__dict_style['[MainFrame:Inactive]']:
                bg = self.__dict_style['[MainFrame:Inactive]']['background']
            if 'border' in self.__dict_style['[MainFrame:Inactive]']:
                bd = self.__style_handler.border_str_to_list(
                    self.__dict_style['[MainFrame:Inactive]']['border'])

        if fullscreen:  # Only borders
            bdr = ['0', '0', '0', '0', '']
            bd = ['0', '0', '0', '0', '#00000000']

        qss = (
            '#CentralShadow {\n'
            '  background-color: rgba(0, 0, 0, 0);\n'
            '  border: 1px solid rgba(0, 0, 0, 0.2);\n'
            f'  border-top-left-radius: {bdr[0]}px;\n'
            f'  border-top-right-radius: {bdr[1]}px;\n'
            f'  border-bottom-left-radius: {bdr[3]}px;\n'
            f'  border-bottom-right-radius: {bdr[2]}px;\n'
            '}\n'
            '#FrameCentralShadow {\n'
            '  background-color: rgba(0, 0, 0, 0);\n'
            '  border: 1px solid rgba(0, 0, 0, 0.2);\n'
            f'  border-radius: {bdr[0]}px;\n'
            '}\n'

            '#CentralBorder {\n'
            '  background-color: rgba(0, 0, 0, 0);\n'
            f'  border-top: {bd[0]}px solid {bd[4]};\n'
            f'  border-right: {bd[1]}px solid {bd[4]};\n'
            f'  border-bottom: {bd[2]}px solid {bd[4]};\n'
            f'  border-left: {bd[3]}px solid {bd[4]};\n'
            f'  border-top-left-radius: {bdr[0]}px;\n'
            f'  border-top-right-radius: {bdr[1]}px;\n'
            f'  border-bottom-left-radius: {bdr[3]}px;\n'
            f'  border-bottom-right-radius: {bdr[2]}px;\n'
            '}\n'
            '#FrameCentralBorder {\n'
            '  background-color: rgba(0, 0, 0, 0);\n'
            f'  border-top: {bd[0]}px solid {bd[4]};\n'
            f'  border-right: {bd[1]}px solid {bd[4]};\n'
            f'  border-bottom: {bd[2]}px solid {bd[4]};\n'
            f'  border-left: {bd[3]}px solid {bd[4]};\n'
            f'  border-radius: {bdr[0]}px;\n'
            '}\n'

            '#Central {\n'
            f'  background-color: {bg};\n  border: 0px;\n'
            f'  border-top-left-radius: {int(bdr[0])-1}px;\n'
            f'  border-top-right-radius: {int(bdr[1])-1}px;\n'
            f'  border-bottom-left-radius: {int(bdr[3])-1}px;\n'
            f'  border-bottom-right-radius: {int(bdr[2])-1}px;\n'
            '}\n'
            '#FrameCentral {\n'
            f'  background-color: {bg};\n  border: 0px;\n'
            f'  border-radius: {int(bdr[0])-1}px;\n'
            '}\n'
            )

        return qss


if __name__ == '__main__':
    st = StyleManager()
