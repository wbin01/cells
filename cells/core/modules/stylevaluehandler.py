#!/usr/bin/env python3


class StyleValueHandler(object):
    def __init__(self):
        pass

    def border_str_to_list(self, border: str) -> list:
        """Parser border str

        '1 1 1 1 rgba(0, 0, 0, 1)'  ->  ['1', '1', '1', 'rgba(0, 0, 0, 1)']
        '1 1 1 1 #FF00F3'           ->  ['1', '1', '1', '#FF00F3']
        """
        border = border.strip().replace('  ', ' ')
        n1, n2, n3, n4, *c = border.replace('px', '').split()
        if '#' in c:
            pass
        else:
            c = ''.join(c).replace(',', ', ')

        return [n1, n2, n3, n4, c]

    def border_list_to_str(self, border: list) -> str:
        """Parser border list

        ['1', '1', '1', '1', 'rgba(0, 0, 0, 1)'] -> '1 1 1 1 rgba(0, 0, 0, 1)'
        ['1', '1', '1', '1', '#FF00F3']          -> '1 1 1 1 #FF00F3'
        """
        return ' '.join(border)

    def border_radius_str_to_list(self, border: str) -> list:
        """Parser border radius str

        '1 1 1 1'  ->  ['1', '1', '1', '1']
        """
        border = border.strip().replace('  ', ' ')
        return border.replace('px', '').split()

    def border_radius_list_to_str(self, border: list) -> str:
        """Parser border radius list

        ['1', '1', '1', '1']  ->  '1 1 1 1'
        """
        return ' '.join(border)

    def margin_padding_str_to_list(self, margin_padding: str) -> list:
        """Parser margin or padding str

        '1 1 1 1'  ->  ['1', '1', '1', '1']
        """
        return self.border_radius_str_to_list(margin_padding)

    def margin_padding_list_to_str(self, margin_padding: list) -> str:
        """Parser margin or padding list

        ['1', '1', '1', '1']  ->  '1 1 1 1'
        """
        return self.border_radius_list_to_str(margin_padding)
