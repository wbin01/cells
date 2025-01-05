#!/usr/bin/env python3
import os
import pathlib

from .iniparse import IniParse
from . import stylemanagerparser as style_parser


class StyleManager(object):
    """Frame style manager."""

    def __init__(self, *args, **kwargs) -> None:
        """Class constructor."""
        super().__init__(*args, **kwargs)
        self.__accent_red = '60'
        self.__accent_green = '140'
        self.__accent_blue = '189'
        self.__accent = '60', '140', '189'

        self.__path = pathlib.Path(__file__).resolve().parent.parent
        self.__url = os.path.join(self.__path, 'static', 'stylerc')
        self.__dict_style = None
        self.__qss_style = None
        self.__style_file = None
        # self.stylesheet = None

    @property
    def accent(self) -> tuple:
        """RGB tuple accent color"""
        return self.__accent

    @accent.setter
    def accent(self, accent: tuple) -> None:
        self.__accent = accent

    @property
    def stylesheet(self) -> dict:
        """Style as dict.

        Get the style as a dictionary or submit a new dictionary style to 
        update it.
        """
        if not self.__dict_style:
            self.__style_file = IniParse(self.__url)
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

    def stylesheet_qss(self) -> dict:
        """Style as qss."""
        if not self.__dict_style:
            self.__style_file = IniParse(self.__url)
            self.stylesheet = self.__style_file.content

        return self.__qss_style

    def style_to_qss(
            self, style: dict = None,
            inactive: bool = False,
            fullscreen: bool = False) -> str:
        """Convert dict style to qss style string.
        
        :param style: dict style. Default is auto.
        :param inactive: True if want inactive style. Default is False.
        :param fullscreen:  True if want fullscreen style. Default is False.
        """

        if not self.__dict_style:
            self.__style_file = IniParse(self.__url)
            self.__dict_style = self.__style_file.content

        style = self.__dict_style if not style else style
        style = self.__expand_style(style)

        qss = ''
        for group_key in style.keys():
            if ':inactive]' in group_key and not inactive:
                continue  # disabled

            if 'background' in style[group_key]:
                background = style[group_key]['background'].replace(
                    'accent_red', self.__accent_red).replace(
                    'accent_green', self.__accent_green).replace(
                    'accent_blue', self.__accent_blue)
            if 'background_image' in style[group_key]:
                if os.name == 'posix':
                    background_image = os.path.expanduser(
                        style[group_key]['background_image'])
                else:
                    background_image = os.path.expandvars(
                        style[group_key]['background_image'])
            if 'border' in style[group_key]:
                border = style[group_key]['border'].replace(
                    'accent_red', self.__accent_red).replace(
                    'accent_green', self.__accent_green).replace(
                    'accent_blue', self.__accent_blue)
                border = style_parser.border_str_to_list(border)
            if 'border_top' in style[group_key]:
                border_top = style[group_key]['border_top'].replace(
                    'accent_red', self.__accent_red).replace(
                    'accent_green', self.__accent_green).replace(
                    'accent_blue', self.__accent_blue)
                border_top = border_top.split('px')
            if 'border_right' in style[group_key]:
                border_right = style[group_key]['border_right'].replace(
                    'accent_red', self.__accent_red).replace(
                    'accent_green', self.__accent_green).replace(
                    'accent_blue', self.__accent_blue)
                border_right = border_right.split('px')
            if 'border_bottom' in style[group_key]:
                border_bottom = style[group_key]['border_bottom'].replace(
                    'accent_red', self.__accent_red).replace(
                    'accent_green', self.__accent_green).replace(
                    'accent_blue', self.__accent_blue)
                border_bottom = border_bottom.split('px')
            if 'border_left' in style[group_key]:
                border_left = style[group_key]['border_left'].replace(
                    'accent_red', self.__accent_red).replace(
                    'accent_green', self.__accent_green).replace(
                    'accent_blue', self.__accent_blue)
                border_left = border_left.split('px')
            if 'border_radius' in style[group_key]:
                border_radius = style[group_key]['border_radius']
                border_radius = style_parser.border_radius_str_to_list(
                    border_radius)
            if 'color' in style[group_key]:
                color = style[group_key]['color'].replace(
                    'accent_red', self.__accent_red).replace(
                    'accent_green', self.__accent_green).replace(
                    'accent_blue', self.__accent_blue)
            if 'margin' in style[group_key]:
                margin = style[group_key]['margin']
                margin = style_parser.margin_padding_str_to_list(margin)
            if 'padding' in style[group_key]:
                padding = style[group_key]['padding']
                padding = style_parser.margin_padding_str_to_list(padding)

            if fullscreen and group_key.startswith('[MainFrame'):
                border = ['0', '0', '0', '0', 'rgba(0, 0, 0, 0.00)']
                border_radius = ['0', '0', '0', '0']

            qss += f'#{group_key.replace(':inactive', '')[1:-1]} ' + '{\n'
            
            if 'background' in style[group_key]:
                qss += f' background-color: {background};\n'
            if 'background_image' in style[group_key]:
                qss += f' background: url({background_image});'  # no-repeat
            if 'border' in style[group_key]:
                qss += (
                    f' border-top: {border[0]}px solid {border[4]};\n'
                    f' border-right: {border[1]}px solid {border[4]};\n'
                    f' border-bottom: {border[2]}px solid {border[4]};\n'
                    f' border-left: {border[3]}px solid {border[4]};\n')
            if 'border_top' in style[group_key]:
                qss += (
                    f' border-top: {border_top[0].strip()}px'
                    f' solid {border_top[1].strip()};\n')
            if 'border_right' in style[group_key]:
                qss += (
                    f' border-right: {border_right[0].strip()}px'
                    f' solid {border_right[1].strip()};\n')
            if 'border_bottom' in style[group_key]:
                qss += (
                    f' border-bottom: {border_bottom[0].strip()}px'
                    f' solid {border_bottom[1].strip()};\n')
            if 'border_left' in style[group_key]:
                qss += (
                    f' border-left: {border_left[0].strip()}px'
                    f' solid {border_left[1].strip()};\n')
            if 'border_radius' in style[group_key]:
                qss += (
                    f' border-top-left-radius: {border_radius[0]}px;\n'
                    f' border-top-right-radius: {border_radius[1]}px;\n'
                    f' border-bottom-left-radius: {border_radius[3]}px;\n'
                    f' border-bottom-right-radius: {border_radius[2]}px;\n')
            if 'color' in style[group_key]:
                qss += f' color: {color};\n'
            if 'margin' in style[group_key] or 'Frame' in group_key:
                qss += (
                    f' margin-top: {margin[0]}px;\n'
                    f' margin-right: {margin[1]}px;\n'
                    f' margin-bottom: {margin[2]}px;\n'
                    f' margin-left: {margin[3]}px;\n')
            if 'padding' in style[group_key]:
                qss += (
                    f' padding-top: {padding[0]}px;\n'
                    f' padding-right: {padding[1]}px;\n'
                    f' padding-bottom: {padding[2]}px;\n'
                    f' padding-left: {padding[3]}px;\n')
            qss += '}\n'

        return qss

    @staticmethod
    def __expand_style(style: dict) -> dict:
        for main_key in style.keys():
            if ':' not in main_key:

                for key in style.keys():
                    if key != main_key and key.startswith(main_key[:-1]):

                        if ('background' not in style[key] and
                            'background' in style[main_key]):
                            style[key]['background'] = style[
                                main_key]['background']

                        if ('border_radius' not in style[key] and
                            'border_radius' in style[main_key]):
                            style[key]['border_radius'] = style[
                                main_key]['border_radius']

                        if ('border' not in style[key] and
                            'border' in style[main_key]):
                            style[key]['border'] = style[main_key]['border']

                        if ('color' not in style[key] and
                            'color' in style[main_key]):
                            style[key]['color'] = style[main_key]['color']

                        if ('margin' not in style[key] and
                            'margin' in style[main_key]):
                            style[key]['margin'] = style[main_key]['margin']

                        if ('padding' not in style[key] and
                            'padding' in style[main_key]):
                            style[key]['padding'] = style[main_key]['padding']
        return style


if __name__ == '__main__':
    st = StyleManager()
