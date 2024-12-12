#!/usr/bin/env python3
import os
import pathlib

from .desktopentryparse import DesktopFile
from . import stylemanagerparser as style_parser


class StyleManager(object):
    """Frame style manager"""

    def __init__(self, *args, **kwargs) -> None:
        """Class constructor"""
        super().__init__(*args, **kwargs)
        self.__path = pathlib.Path(__file__).resolve().parent
        self.__url = os.path.join(self.__path, 'static', 'stylerc')
        
        self.__dict_style = None
        self.__qss_style = None

        self.__style_file = None
        self.stylesheet = None

    @property
    def stylesheet(self) -> dict:
        """Style as dict

        Get the style as a dictionary or submit a new dictionary style to 
        update it
        """
        if not self.__dict_style:
            self.__style_file = DesktopFile(self.__url)
            self.__dict_style = self.__style_file.content

        return self.__dict_style
    
    @stylesheet.setter
    def stylesheet(self, style: dict) -> None:
        self.__dict_style = style
        self.__qss_style = {
            'active': self.style_to_qss(),
            'inactive': self.style_to_qss(inactive=True),
            'fullscreen': self.style_to_qss(fullscreen=True),
            'inactive_fullscreen': self.style_to_qss(
                inactive=True, fullscreen=True)}

    def stylesheet_for_qss(self) -> dict:
        """..."""
        if not self.__dict_style:
            self.__style_file = DesktopFile(self.__url)
            self.stylesheet = self.__style_file.content

        return self.__qss_style

    def style_to_qss(
            self, style: dict = None,
            inactive: bool = False,
            fullscreen: bool = False) -> str:

        if not self.__dict_style:
            self.__style_file = DesktopFile(self.__url)
            self.__dict_style = self.__style_file.content

        style = self.__dict_style if not style else style
        qss = ''
        for group_key in style.keys():
            if group_key == '[MainFrame:inactive]' and not inactive:
                continue  # disabled
            background = 'rgba(0, 0, 0, 0.00)'
            border = '0px 0px 0px 0px rgba(0, 0, 0, 0.00)'
            border_radius = '0px 0px 0px 0px'
            color = 'rgba(230, 230, 230, 1.00)'
            margin = '0px 0px 0px 0px'
            padding = '0px 0px 0px 0px'

            if 'background' in style[group_key]:
                background = style[group_key]['background']
            if 'border' in style[group_key]:
                border = style[group_key]['border']
            if 'border_radius' in style[group_key]:
                border_radius = style[group_key]['border_radius']
            if 'color' in style[group_key]:
                color = style[group_key]['color']
            if 'margin' in style[group_key]:
                margin = style[group_key]['margin']
            if 'padding' in style[group_key]:
                padding = style[group_key]['padding']

            border = style_parser.border_str_to_list(border)
            border_radius = style_parser.border_radius_str_to_list(border_radius)
            margin = style_parser.margin_padding_str_to_list(margin)
            padding = style_parser.margin_padding_str_to_list(padding)

            if 'Frame' in group_key:
                border_radius = [
                    int(border_radius[0]) -1,
                    int(border_radius[1]) -1,
                    int(border_radius[2]) -1,
                    int(border_radius[3]) -1]

            if fullscreen and group_key.startswith('[MainFrame'):
                border = ['0', '0', '0', '0', 'rgba(0, 0, 0, 0.00)']
                border_radius = ['0', '0', '0', '0']

            qss += f'#{group_key.replace(':inactive', '')[1:-1]} ' + '{\n'
            
            if 'background' in style[group_key]:
                qss += f'  background-color: {background};\n'
            if 'border' in style[group_key]:
                qss += (
                    f'  border-top: {border[0]}px solid {border[4]};\n'
                    f'  border-right: {border[1]}px solid {border[4]};\n'
                    f'  border-bottom: {border[2]}px solid {border[4]};\n'
                    f'  border-left: {border[3]}px solid {border[4]};\n')
            if 'border_radius' in style[group_key]:
                qss += (
                    f'  border-top-left-radius: {border_radius[0]}px;\n'
                    f'  border-top-right-radius: {border_radius[1]}px;\n'
                    f'  border-bottom-left-radius: {border_radius[3]}px;\n'
                    f'  border-bottom-right-radius: {border_radius[2]}px;\n')
            if 'color' in style[group_key]:
                qss += f'  color: {color};\n'
            if 'margin' in style[group_key]:
                qss += (
                    f'  margin-top: {margin[0]}px;\n'
                    f'  margin-right: {margin[1]}px;\n'
                    f'  margin-bottom: {margin[2]}px;\n'
                    f'  margin-left: {margin[3]}px;\n')
            if 'padding' in style[group_key]:
                qss += (
                    f'  padding-top: {padding[0]}px;\n'
                    f'  padding-right: {padding[1]}px;\n'
                    f'  padding-bottom: {padding[2]}px;\n'
                    f'  padding-left: {padding[3]}px;\n')
            qss += '}\n'
        
        return qss


if __name__ == '__main__':
    st = StyleManager()
