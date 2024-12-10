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
        self.style_ids = {}

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
            'fullscreen': self.__dict_style_to_qss_str(fullscreen=True),
            'inactive_fullscreen': self.__dict_style_to_qss_str(
                inactive=True, fullscreen=True)}

    def stylesheet_for_qss(self) -> dict:
        """..."""
        return self.__qss_style

    def __style_to_qss(
            self, inactive: bool = False, fullscreen: bool = False) -> str:
        # disabled
        background = 'rgba(0, 0, 0, 0.00)'
        border = '0px 0px 0px 0px rgba(0, 0, 0, 0.00)'
        border_radius = '0px 0px 0px 0px'
        color = 'rgba(230, 230, 230, 1.00)'
        margin = '0px 0px 0px 0px'
        padding = '0px 0px 0px 0px'

        qss = ''
        for group_key in style.keys():
            if inactive:
                ok = False if ':inactive' not in group_key else True
            else:
                ok = False if ':inactive' in group_key else True

            if ok:
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

            # if fullscreen:  # Only borders
            #     border = ['0', '0', '0', '0', 'rgba(0, 0, 0, 0.00)']
            #     border_radius = ['0', '0', '0', '0']

            qss += (
                f'#{group_key.replace(':inactive', '')} ' '{\n'
                f'  background-color: {background};\n'
                f'  color: {color};\n'
                f'  border-top: {border[0]}px solid {border[4]};\n'
                f'  border-right: {border[1]}px solid {border[4]};\n'
                f'  border-bottom: {border[2]}px solid {border[4]};\n'
                f'  border-left: {border[3]}px solid {border[4]};\n'
                f'  border-top-left-radius: {border_radius[0]}px;\n'
                f'  border-top-right-radius: {border_radius[1]}px;\n'
                f'  border-bottom-left-radius: {border_radius[3]}px;\n'
                f'  border-bottom-right-radius: {border_radius[2]}px;\n'
                f'  margin-top: {margin[0]}px;\n'
                f'  margin-right: {margin[1]}px;\n'
                f'  margin-bottom: {margin[2]}px;\n'
                f'  margin-left: {margin[3]}px;\n'
                f'  padding-top: {padding[0]}px;\n'
                f'  padding-right: {padding[1]}px;\n'
                f'  padding-bottom: {padding[2]}px;\n'
                f'  padding-left: {padding[3]}px;\n'
                '}\n'
                )
            """
            qss = (
            '#MainFrameShadow {\n'
            '  background-color: rgba(0, 0, 0, 0.00);\n'
            f'  border: {bd_shadow};\n'
            f'  border-top-left-radius: {bdr[0]}px;\n'
            f'  border-top-right-radius: {bdr[1]}px;\n'
            f'  border-bottom-left-radius: {bdr[3]}px;\n'
            f'  border-bottom-right-radius: {bdr[2]}px;\n'
            '}\n'
            '#MainFrameBorder {\n'
            '  background-color: rgba(0, 0, 0, 0.0);\n'
            f'  border-top: {bd[0]}px solid {bd[4]};\n'
            f'  border-right: {bd[1]}px solid {bd[4]};\n'
            f'  border-bottom: {bd[2]}px solid {bd[4]};\n'
            f'  border-left: {bd[3]}px solid {bd[4]};\n'
            f'  border-top-left-radius: {bdr[0]}px;\n'
            f'  border-top-right-radius: {bdr[1]}px;\n'
            f'  border-bottom-left-radius: {bdr[3]}px;\n'
            f'  border-bottom-right-radius: {bdr[2]}px;\n'
            '}\n'
            '#MainFrameCentral {\n'
            f'  background-color: {bg};\n  border: 0px;\n'
            f'  border-top-left-radius: {int(bdr[0])-1}px;\n'
            f'  border-top-right-radius: {int(bdr[1])-1}px;\n'
            f'  border-bottom-left-radius: {int(bdr[3])-1}px;\n'
            f'  border-bottom-right-radius: {int(bdr[2])-1}px;\n'
            f'  padding-top: {pd[0]}px;\n'
            f'  padding-right: {pd[1]}px;\n'
            f'  padding-bottom: {pd[2]}px;\n'
            f'  padding-left: {pd[3]}px;\n'
            '}\n'
            )
            """
        return ''

    def __dict_style_to_qss_str(
            self, inactive: bool = False, fullscreen: bool = False) -> str:
        # https://doc.qt.io/qt-5/stylesheet-reference.html
        # https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qpushbutton
        qss = ''
        for name in self.__dict_style.keys():
            name = name.split(':')[0][1:].rstrip(']')
            if name.startswith('Button'):
                qss += self.qss_button(name=name, inactive=inactive)
            elif name.startswith('Frame'):
                qss += self.qss_frame()
            elif name.startswith('Label'):
                qss += self.qss_label(inactive=inactive)
            elif name.startswith('MainFrame'):
                qss += self.qss_main_frame(inactive=inactive, fullscreen=fullscreen)
            elif name.startswith('Widget'):
                qss += self.qss_widget(name=name, inactive=inactive)
        return qss

    def qss_button(
            self,
            name: str = 'Button',
            dict_style: dict = None,
            inactive: bool = False,
            only_normal: bool = False,
            only_hover: bool = False,
            only_pressed: bool = False,) -> str:
        """..."""
        dict_style = self.__dict_style if not dict_style else dict_style
        name_id = name.split('.')[1] if '.' in name else name

        bg = dict_style[f'[{name}]']['background']
        cl = dict_style[f'[{name}]']['color']
        bd = style_parser.border_str_to_list(dict_style[f'[{name}]']['border'])
        bdr = style_parser.border_radius_str_to_list(
            dict_style[f'[{name}]']['border radius'])
        mg = style_parser.margin_padding_str_to_list(
            dict_style[f'[{name}]']['margin'])
        pd = style_parser.margin_padding_str_to_list(
            dict_style[f'[{name}]']['padding'])

        if inactive:  # Only colors
            if 'background' in dict_style[f'[{name}:inactive]']:
                bg = dict_style[f'[{name}:inactive]']['background']
            if 'color' in dict_style[f'[{name}:inactive]']:
                cl = dict_style[f'[{name}:inactive]']['color']
            if 'border' in dict_style[f'[{name}:inactive]']:
                bd = style_parser.border_str_to_list(
                    dict_style[f'[{name}:inactive]']['border'])
        qss = (
            f'#{name_id} ' '{\n'
            f'  background-color: {bg};\n'
            f'  border-top: {bd[0]}px solid {bd[4]};\n'
            f'  border-right: {bd[1]}px solid {bd[4]};\n'
            f'  border-bottom: {bd[2]}px solid {bd[4]};\n'
            f'  border-left: {bd[3]}px solid {bd[4]};\n'
            f'  border-top-left-radius: {bdr[0]}px;\n'
            f'  border-top-right-radius: {bdr[1]}px;\n'
            f'  border-bottom-left-radius: {bdr[3]}px;\n'
            f'  border-bottom-right-radius: {bdr[2]}px;\n'
            f'  margin-top: {mg[0]}px;\n'
            f'  margin-right: {mg[1]}px;\n'
            f'  margin-bottom: {mg[2]}px;\n'
            f'  margin-left: {mg[3]}px;\n'
            f'  padding-top: {pd[0]}px;\n'
            f'  padding-right: {pd[1]}px;\n'
            f'  padding-bottom: {pd[2]}px;\n'
            f'  padding-left: {pd[3]}px;\n'
            '}\n'
            f'#{name_id}Label ' '{\n'
            f'  color: {cl};\n'
            '  background-color: rgba(0, 0, 0, 0.0);\n'
            '  border: 0px solid rgba(0, 0, 0, 0.0);\n'
            '}\n'
            )

        if only_normal:
            return qss

        if not inactive:
            if 'background' in dict_style[f'[{name}:hover]']:
                bg = dict_style[f'[{name}:hover]']['background']
            if 'color' in dict_style[f'[{name}:hover]']:
                cl = dict_style[f'[{name}:hover]']['color']
            if 'border' in dict_style[f'[{name}:hover]']:
                bd = style_parser.border_str_to_list(
                    dict_style[f'[{name}:hover]']['border'])
            if 'border radius' in dict_style[f'[{name}:hover]']:
                bdr = style_parser.border_radius_str_to_list(
                    dict_style[f'[{name}:hover]']['border radius'])
        hover = (
            f'#{name_id}:hover ' '{\n'
            f'  background-color: {bg};\n'
            f'  border-top: {bd[0]}px solid {bd[4]};\n'
            f'  border-right: {bd[1]}px solid {bd[4]};\n'
            f'  border-bottom: {bd[2]}px solid {bd[4]};\n'
            f'  border-left: {bd[3]}px solid {bd[4]};\n'
            f'  border-top: {bd[0]}px solid {bd[4]};\n'
            f'  border-right: {bd[1]}px solid {bd[4]};\n'
            f'  border-bottom: {bd[2]}px solid {bd[4]};\n'
            f'  border-left: {bd[3]}px solid {bd[4]};\n'
            f'  border-top-left-radius: {bdr[0]}px;\n'
            f'  border-top-right-radius: {bdr[1]}px;\n'
            f'  border-bottom-left-radius: {bdr[3]}px;\n'
            f'  border-bottom-right-radius: {bdr[2]}px;\n'
            '}\n'
            f'#{name_id}Label:hover ' '{\n'
            f'  color: {cl};\n'
            '  background-color: rgba(0, 0, 0, 0.0);\n'
            '  border: 0px solid rgba(0, 0, 0, 0.0);\n'
            '}\n'
            )
        qss += hover

        if only_hover:
            return hover
        
        if not inactive:
            if 'background' in dict_style[f'[{name}:pressed]']:
                bg = dict_style[f'[{name}:pressed]']['background']
            if 'color' in dict_style[f'[{name}:pressed]']:
                cl = dict_style[f'[{name}:pressed]']['color']
            if 'border' in dict_style[f'[{name}:pressed]']:
                bd = style_parser.border_str_to_list(
                    dict_style[f'[{name}:pressed]']['border'])
            if 'border radius' in dict_style[f'[{name}:pressed]']:
                bdr = style_parser.border_radius_str_to_list(
                    dict_style[f'[{name}:pressed]']['border radius'])
        pressed = (
            f'#{name_id}:pressed ' '{\n'
            f'  background-color: {bg};\n'
            f'  border-top: {bd[0]}px solid {bd[4]};\n'
            f'  border-right: {bd[1]}px solid {bd[4]};\n'
            f'  border-bottom: {bd[2]}px solid {bd[4]};\n'
            f'  border-left: {bd[3]}px solid {bd[4]};\n'
            f'  border-top-left-radius: {bdr[0]}px;\n'
            f'  border-top-right-radius: {bdr[1]}px;\n'
            f'  border-bottom-left-radius: {bdr[3]}px;\n'
            f'  border-bottom-right-radius: {bdr[2]}px;\n'
            '}\n'
            f'#{name_id}Label:pressed ' '{\n'
            f'  color: {cl};\n'
            '  background-color: rgba(0, 0, 0, 0.0);\n'
            '  border: 0px solid rgba(0, 0, 0, 0.0);\n'
            '}\n'
            )
        qss += pressed

        if only_pressed:
            return pressed

        return qss

    def qss_frame(self) -> str:
        bg = self.__dict_style['[Frame]']['background']
        bd = style_parser.border_str_to_list(
            self.__dict_style['[Frame]']['border'])
        bdr = style_parser.border_radius_str_to_list(
            self.__dict_style['[Frame]']['border radius'])
        pd = style_parser.margin_padding_str_to_list(
            self.__dict_style['[Frame]']['padding'])

        qss = (
            '#FrameShadow {\n'
            '  background-color: rgba(0, 0, 0, 0);\n'
            '  border: 1px solid rgba(0, 0, 0, 0.2);\n'
            f'  border-radius: {bdr[0]}px;\n'
            '}\n'
            '#FrameBorder {\n'
            '  background-color: rgba(0, 0, 0, 0);\n'
            f'  border-top: {bd[0]}px solid {bd[4]};\n'
            f'  border-right: {bd[1]}px solid {bd[4]};\n'
            f'  border-bottom: {bd[2]}px solid {bd[4]};\n'
            f'  border-left: {bd[3]}px solid {bd[4]};\n'
            f'  border-radius: {bdr[0]}px;\n'
            '}\n'
            '#FrameCentral {\n'
            f'  background-color: {bg};\n  border: 0px;\n'
            f'  border-radius: {int(bdr[0])-1}px;\n'
            f'  padding-top: {pd[0]}px;\n'
            f'  padding-right: {pd[1]}px;\n'
            f'  padding-bottom: {pd[2]}px;\n'
            f'  padding-left: {pd[3]}px;\n'
            '}\n'
            )
        return qss

    def qss_label(self, inactive: bool = False) -> str:
        bg = self.__dict_style['[Label]']['background']
        cl = self.__dict_style['[Label]']['color']
        bd = style_parser.border_str_to_list(
            self.__dict_style['[Label]']['border'])
        bdr = style_parser.border_radius_str_to_list(
            self.__dict_style['[Label]']['border radius'])
        mg = style_parser.margin_padding_str_to_list(
            self.__dict_style['[Label]']['margin'])
        pd = style_parser.margin_padding_str_to_list(
            self.__dict_style['[Label]']['padding'])

        if inactive:  # Only colors
            if 'background' in self.__dict_style['[Label:inactive]']:
                bg = self.__dict_style['[Label:inactive]']['background']
            if 'color' in self.__dict_style['[Label:inactive]']:
                cl = self.__dict_style['[Label:inactive]']['color']
            if 'border' in self.__dict_style['[Label:inactive]']:
                bd = style_parser.border_str_to_list(
                    self.__dict_style['[Label:inactive]']['border'])
        qss = (
            '#Label {\n'
            f'  background-color: {bg};\n'
            f'  color: {cl};\n'
            f'  border-top: {bd[0]}px solid {bd[4]};\n'
            f'  border-right: {bd[1]}px solid {bd[4]};\n'
            f'  border-bottom: {bd[2]}px solid {bd[4]};\n'
            f'  border-left: {bd[3]}px solid {bd[4]};\n'
            f'  border-top-left-radius: {bdr[0]}px;\n'
            f'  border-top-right-radius: {bdr[1]}px;\n'
            f'  border-bottom-left-radius: {bdr[3]}px;\n'
            f'  border-bottom-right-radius: {bdr[2]}px;\n'
            f'  margin-top: {mg[0]}px;\n'
            f'  margin-right: {mg[1]}px;\n'
            f'  margin-bottom: {mg[2]}px;\n'
            f'  margin-left: {mg[3]}px;\n'
            f'  padding-top: {pd[0]}px;\n'
            f'  padding-right: {pd[1]}px;\n'
            f'  padding-bottom: {pd[2]}px;\n'
            f'  padding-left: {pd[3]}px;\n'
            '}\n'
            )
        if 'background' in self.__dict_style['[Label:hover]']:
            bg = self.__dict_style['[Label:hover]']['background']
        if 'color' in self.__dict_style['[Label:hover]']:
            cl = self.__dict_style['[Label:hover]']['color']
        if 'border' in self.__dict_style['[Label:hover]']:
            bd = style_parser.border_str_to_list(
                self.__dict_style['[Label:hover]']['border'])
        if 'border radius' in self.__dict_style['[Label:hover]']:
            bdr = style_parser.border_radius_str_to_list(
                self.__dict_style['[Label:hover]']['border radius'])
        qss += (
            '#Label:hover {\n'
            f'  background-color: {bg};\n'
            f'  color: {cl};\n'
            f'  border-top: {bd[0]}px solid {bd[4]};\n'
            f'  border-right: {bd[1]}px solid {bd[4]};\n'
            f'  border-bottom: {bd[2]}px solid {bd[4]};\n'
            f'  border-left: {bd[3]}px solid {bd[4]};\n'
            f'  border-top: {bd[0]}px solid {bd[4]};\n'
            f'  border-right: {bd[1]}px solid {bd[4]};\n'
            f'  border-bottom: {bd[2]}px solid {bd[4]};\n'
            f'  border-left: {bd[3]}px solid {bd[4]};\n'
            f'  border-top-left-radius: {bdr[0]}px;\n'
            f'  border-top-right-radius: {bdr[1]}px;\n'
            f'  border-bottom-left-radius: {bdr[3]}px;\n'
            f'  border-bottom-right-radius: {bdr[2]}px;\n'
            '}\n'
            )
        return qss

    def qss_main_frame(self, inactive: bool = False, fullscreen: bool = False) -> str:
        bg = self.__dict_style['[MainFrame]']['background']
        bd = style_parser.border_str_to_list(
            self.__dict_style['[MainFrame]']['border'])
        bdr = style_parser.border_radius_str_to_list(
            self.__dict_style['[MainFrame]']['border radius'])
        pd = style_parser.margin_padding_str_to_list(
            self.__dict_style['[MainFrame]']['padding'])
        bd_shadow = '1px solid rgba(0, 0, 0, 0.30)'

        if inactive:  # Only colors
            if 'background' in self.__dict_style['[MainFrame:inactive]']:
                bg = self.__dict_style['[MainFrame:inactive]']['background']
            if 'border' in self.__dict_style['[MainFrame:inactive]']:
                bd = style_parser.border_str_to_list(
                    self.__dict_style['[MainFrame:inactive]']['border'])

        if fullscreen:  # Only borders
            bdr = ['0', '0', '0', '0']
            bd = ['0', '0', '0', '0', 'rgba(0, 0, 0, 0.00)']
            bd_shadow = '0px solid rgba(0, 0, 0, 0.00)'

        qss = (
            '#MainFrameShadow {\n'
            '  background-color: rgba(0, 0, 0, 0.00);\n'
            f'  border: {bd_shadow};\n'
            f'  border-top-left-radius: {bdr[0]}px;\n'
            f'  border-top-right-radius: {bdr[1]}px;\n'
            f'  border-bottom-left-radius: {bdr[3]}px;\n'
            f'  border-bottom-right-radius: {bdr[2]}px;\n'
            '}\n'
            '#MainFrameBorder {\n'
            '  background-color: rgba(0, 0, 0, 0.0);\n'
            f'  border-top: {bd[0]}px solid {bd[4]};\n'
            f'  border-right: {bd[1]}px solid {bd[4]};\n'
            f'  border-bottom: {bd[2]}px solid {bd[4]};\n'
            f'  border-left: {bd[3]}px solid {bd[4]};\n'
            f'  border-top-left-radius: {bdr[0]}px;\n'
            f'  border-top-right-radius: {bdr[1]}px;\n'
            f'  border-bottom-left-radius: {bdr[3]}px;\n'
            f'  border-bottom-right-radius: {bdr[2]}px;\n'
            '}\n'
            '#MainFrameCentral {\n'
            f'  background-color: {bg};\n  border: 0px;\n'
            f'  border-top-left-radius: {int(bdr[0])-1}px;\n'
            f'  border-top-right-radius: {int(bdr[1])-1}px;\n'
            f'  border-bottom-left-radius: {int(bdr[3])-1}px;\n'
            f'  border-bottom-right-radius: {int(bdr[2])-1}px;\n'
            f'  padding-top: {pd[0]}px;\n'
            f'  padding-right: {pd[1]}px;\n'
            f'  padding-bottom: {pd[2]}px;\n'
            f'  padding-left: {pd[3]}px;\n'
            '}\n'
            )
        return qss

    def qss_widget(
            self,
            name: str = 'Widget',
            dict_style: dict = None,
            inactive: bool = False,
            only_normal: bool = False,
            only_hover: bool = False) -> str:
        """..."""
        dict_style = self.__dict_style if not dict_style else dict_style
        name_id = name.split('.')[1] if '.' in name else name

        bg = dict_style[f'[{name}]']['background']
        bd = style_parser.border_str_to_list(
            dict_style[f'[{name}]']['border'])
        bdr = style_parser.border_radius_str_to_list(
            dict_style[f'[{name}]']['border radius'])
        mg = style_parser.margin_padding_str_to_list(
            dict_style[f'[{name}]']['margin'])
        pd = style_parser.margin_padding_str_to_list(
            dict_style[f'[{name}]']['padding'])

        if inactive:  # Only colors
            if 'background' in dict_style[f'[{name}:inactive]']:
                bg = dict_style[f'[{name}:inactive]']['background']
            if 'border' in dict_style[f'[{name}:inactive]']:
                bd = style_parser.border_str_to_list(
                    dict_style[f'[{name}:inactive]']['border'])
        qss = (
            f'#{name_id} ' '{\n'
            f'  background-color: {bg};\n'
            f'  border-top: {bd[0]}px solid {bd[4]};\n'
            f'  border-right: {bd[1]}px solid {bd[4]};\n'
            f'  border-bottom: {bd[2]}px solid {bd[4]};\n'
            f'  border-left: {bd[3]}px solid {bd[4]};\n'
            f'  border-top-left-radius: {bdr[0]}px;\n'
            f'  border-top-right-radius: {bdr[1]}px;\n'
            f'  border-bottom-left-radius: {bdr[3]}px;\n'
            f'  border-bottom-right-radius: {bdr[2]}px;\n'
            f'  margin-top: {mg[0]}px;\n'
            f'  margin-right: {mg[1]}px;\n'
            f'  margin-bottom: {mg[2]}px;\n'
            f'  margin-left: {mg[3]}px;\n'
            f'  padding-top: {pd[0]}px;\n'
            f'  padding-right: {pd[1]}px;\n'
            f'  padding-bottom: {pd[2]}px;\n'
            f'  padding-left: {pd[3]}px;\n'
            '}\n'
            )

        if only_normal:
            return qss

        if not inactive:
            if 'background' in dict_style[f'[{name}:hover]']:
                bg = dict_style[f'[{name}:hover]']['background']
            if 'border' in dict_style[f'[{name}:hover]']:
                bd = style_parser.border_str_to_list(
                    dict_style[f'[{name}:hover]']['border'])
            if 'border radius' in dict_style[f'[{name}:hover]']:
                bdr = style_parser.border_radius_str_to_list(
                    dict_style[f'[{name}:hover]']['border radius'])
        hover = (
            f'#{name_id}:hover ' '{\n'
            f'  background-color: {bg};\n'
            f'  border-top: {bd[0]}px solid {bd[4]};\n'
            f'  border-right: {bd[1]}px solid {bd[4]};\n'
            f'  border-bottom: {bd[2]}px solid {bd[4]};\n'
            f'  border-left: {bd[3]}px solid {bd[4]};\n'
            f'  border-top: {bd[0]}px solid {bd[4]};\n'
            f'  border-right: {bd[1]}px solid {bd[4]};\n'
            f'  border-bottom: {bd[2]}px solid {bd[4]};\n'
            f'  border-left: {bd[3]}px solid {bd[4]};\n'
            f'  border-top-left-radius: {bdr[0]}px;\n'
            f'  border-top-right-radius: {bdr[1]}px;\n'
            f'  border-bottom-left-radius: {bdr[3]}px;\n'
            f'  border-bottom-right-radius: {bdr[2]}px;\n'
            '}\n'
            )
        qss += hover

        if only_hover:
            return hover

        return qss


if __name__ == '__main__':
    st = StyleManager()
