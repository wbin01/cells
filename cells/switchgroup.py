#!/usr/bin/env python3
from .checkgroup import CheckGroup


class SwitchGroup(CheckGroup):
    """Switch Buttons Group Widget."""
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.style_id = 'SwitchGroup'

    def __str__(self) -> str:
        return f'<SwitchGroup: {id(self)}>'
