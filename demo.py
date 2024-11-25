#!/usr/bin/env python3
import os
import sys

from cells import Application, MainFrame, Frame


if __name__ == '__main__':
    app = Application(sys.argv)
    app.frame = MainFrame()
    app.frame_id = [__file__, 'cells', 'Cells']
    app.icon = f'{os.environ['HOME']}/Dev/GitLab/cells/icon.svg'
    app.exec()
