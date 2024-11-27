#!/usr/bin/env python3
from .core import CoreSignal


class Signal(CoreSignal):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
