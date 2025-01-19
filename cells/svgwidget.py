#!/usr/bin/env python3
from PySide6 import QtCore, QtSvgWidgets
from __feature__ import snake_case

from .event import Event
from .widget import Widget


class SvgWidget(Widget):
    """Svg Widget."""
    def __init__(self, path: str = None, *args, **kwargs) -> None:
        """Class constructor."""
        super().__init__(*args, **kwargs)
        self.__path = path
        self._obj = QtSvgWidgets.QSvgWidget()
        self.style_id = 'SvgWidget'
        self.height, self.width = 16, 16
        self.__state = None

        self.__normal_style = None
        self.__hover_style = None
        self.__pressed_style = None
        self.__inactive_style = None

        self.signal(Event.MAIN_PARENT).connect(self.__on_main_parent)
        self.signal(Event.STYLE).connect(self.__on_style)
        self.signal(Event.STYLE_ID).connect(self.__on_style_id)
        self.signal(Event.STYLE_CLASS).connect(self.__on_style_id)

    @property
    def state(self) -> str:
        """..."""
        return self.__state

    @state.setter
    def state(self, state: str = None) -> None:
        self.__state = state
        state = '' if not state else ':' + state

        if not self.__path or not self._main_parent:
            return

        if not self.__state:
            style = self.__normal_style
        elif self.__state == 'hover':
            style = self.__hover_style
        elif self.__state == 'pressed':
            style = self.__pressed_style
        else:
            style = self.__inactive_style

        with open(self.__path, "r") as f:
            content = f.read()

        r, g, b, a = self.__border_or_color_to_rgba_list(style['border'])
        border = f'#{int(r):02X}{int(g):02X}{int(b):02X}'
        content = self.__replace_color('border', border, a, content)

        r, g, b, a = self.__border_or_color_to_rgba_list(style['color'])
        color = f'#{int(r):02X}{int(g):02X}{int(b):02X}'
        content = self.__replace_color('color', color, a, content)

        r, g, b, a = self.__border_or_color_to_rgba_list(style['background'])
        background = f'#{int(r):02X}{int(g):02X}{int(b):02X}'
        content = self.__replace_color('background', background, a, content)

        self._obj.load(QtCore.QByteArray(content.encode('utf-8')))

    def load(self, path: str) -> None:
        self.__path = path
        self._obj.load(QtCore.QByteArray(self.__path.encode('utf-8')))

    @staticmethod
    def __border_or_color_to_rgba_list(border: str) -> list:
        # 1 rgb 0 0 0 0.00 | 1 rgb 0 0 0 | 1 #000000
        # rgb 0 0 0 0.00   | rgb 0 0 0   | #000000
        bd = border.replace('accent_red', '60').replace('accent_green', '140'
            ).replace('accent_blue', '189').replace('px', '').replace('a(', ' '
            ).replace('(', ' ').replace(')', '').replace(',', '')

        # ['1 ', '0 0 0 0.00'] | ['1 ', '0 0 0'] | ['1 ', '000000']
        sep = '#' if '#' in bd else 'rgb'
        color = bd.replace('  ', ' ').strip().split(sep)[-1]

        if sep == '#':
            if len(color) == 3:  # 000
                r, g, b = color[0], color[1], color[2]
                r, g, b = int(r + r, 16), int(g + g, 16), int(b + b, 16)
                a = 1.0
            
            else:  # 000000 | 00000000
                color += 'ff'
                r, g = int(color[:2], 16), int(color[2:4], 16)
                b, a = int(color[4:6], 16), round(int(color[6:8], 16) / 255, 2)
        
        else:  # '0 0 0 0.00' | '0 0 0'
            color = color.replace('  ', ' ').strip().split()

            if len(color) == 4:  # ['0', '0', '0', '0.00']
                r, g, b = int(color[0]), int(color[1]), int(color[2])
                a = round(float(color[3]), 2)
            else:
                r, g, b = int(color[0]), int(color[1]), int(color[2])
                a = 1.0

        return [r, g, b, a]

    def __on_main_parent(self) -> None:
        self._main_parent.signal(Event.FOCUS_IN).connect(self.__on_style)
        self._main_parent.signal(Event.FOCUS_OUT).connect(self.__on_style)

    def __on_style(self):
        if not self._main_parent:
            return
        qss = ''
        for state in ['', ':hover', ':pressed', ':inactive']:
            qss += (
                f'#{self.style_id}{state} ' '{\n'
                ' background: rgba(0, 0, 0, 0.0);\n'
                ' margin: 0px;\n'
                ' padding: 0px;\n'
                ' color: rgba(0, 0, 0, 0.0);\n'
                ' border: 1px rgba(0, 0, 0, 0.0);\n}\n')
        self._obj.set_style_sheet(qss)

    def __on_style_id(self):
        if not self._main_parent:
            return

        self.__normal_style = {
            'background':
                self.style[f'[{self.style_id}]']['background'],
            'color': self.style[f'[{self.style_id}]']['color'],
            'border': self.style[f'[{self.style_id}]']['border']}
        self.__hover_style = {
            'background':
                self.style[f'[{self.style_id}:hover]']['background'],
            'color': self.style[f'[{self.style_id}:hover]']['color'],
            'border': self.style[f'[{self.style_id}:hover]']['border']}
        self.__pressed_style = {
            'background':
                self.style[f'[{self.style_id}:pressed]']['background'],
            'color': self.style[f'[{self.style_id}:pressed]']['color'],
            'border': self.style[f'[{self.style_id}:pressed]']['border']}
        self.__inactive_style = {
            'background':
                self.style[f'[{self.style_id}:inactive]']['background'],
            'color': self.style[f'[{self.style_id}:inactive]']['color'],
            'border': self.style[f'[{self.style_id}:inactive]']['border']}

    @staticmethod
    def __replace_color(id_color, color, alpha, content) -> str:
        new_scopes = []
        for scope in content.split('>'):
            if f'id="{id_color}"' in scope:

                new_props = []
                found_color = False
                found_alpha = False
                for prop in scope.split():

                    if prop.startswith('fill="'):
                        prop = f'fill="{color}"'
                        found_color = True

                    elif prop.startswith('fill-opacity="'):
                        prop = f'fill-opacity="{alpha}"' 
                        found_alpha = True
                        
                    new_props.append(prop)

                if not found_color:
                    new_props[1] = new_props[1] + f' fill="{color}"'

                if not found_alpha:
                    new_props[1] = new_props[1] + f' fill-opacity="{alpha}"'


                new_scopes.append(' '.join(new_props))
            else:
                new_scopes.append(scope)

        break_mark = '-///*Bilbo_Baggins*///-'
        new_content = f'>{break_mark}'.join(new_scopes).replace('\n', '')
        return new_content.replace(break_mark, '\n')

    def __str__(self) -> str:
        return f'<SvgWidget: {id(self)}>'
