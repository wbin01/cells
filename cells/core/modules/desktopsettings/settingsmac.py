#!/usr/bin/env python3
from PySide6 import QtGui
from __feature__ import snake_case

from . import settingsbase
from .. import cli


class EnvSettingsMac(settingsbase.EnvSettings):
    """..."""

    def __init__(self, *args, **kwargs) -> None:
        """..."""
        super().__init__(*args, **kwargs)

