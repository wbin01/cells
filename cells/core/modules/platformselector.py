#!/usr/bin/env python3
import os
import platform


class PlatformSelector(object):
    """..."""

    def __init__(self):
        """..."""
        # linux bsd mac windows unknown
        self.__operational_system = self.__os()

        # plasma gnome cinnamon xfce mac
        # windows-7 windows-10 windows-11 unknown
        self.__desktop_environment = self.__de()

    @property
    def desktop_environment(self) -> str:
        """Desktop environment name"""
        return self.__desktop_environment

    @desktop_environment.setter
    def desktop_environment(self, desktop_environment_name: str) -> None:
        self.__desktop_environment = desktop_environment_name

    @property
    def operational_system(self) -> str:
        """Operational system name"""
        return self.__operational_system

    @operational_system.setter
    def operational_system(self, operational_system_name: str) -> None:
        self.__operational_system = operational_system_name

    def __de(self) -> str:
        # ...
        if self.__operational_system == 'linux':
            if (os.environ['DESKTOP_SESSION'] == 'plasma' or
                    os.environ['XDG_SESSION_DESKTOP'] == 'KDE' or
                    os.environ['XDG_CURRENT_DESKTOP'] == 'KDE'):
                return 'plasma'

            if (os.environ['DESKTOP_SESSION'] == 'cinnamon' or
                    os.environ['XDG_SESSION_DESKTOP'] == 'cinnamon' or
                    os.environ['XDG_CURRENT_DESKTOP'] == 'X-Cinnamon'):
                return 'cinnamon'

            if (os.environ['DESKTOP_SESSION'] == 'xubuntu' or
                    os.environ['XDG_SESSION_DESKTOP'] == 'xubuntu' or
                    os.environ['XDG_CURRENT_DESKTOP'] == 'XFCE'):
                return 'xfce'

            if (os.environ['DESKTOP_SESSION'] == 'mate' or
                    os.environ['XDG_SESSION_DESKTOP'] == 'mate' or
                    os.environ['XDG_CURRENT_DESKTOP'] == 'MATE'):
                return 'mate'

            return 'gnome'

        elif self.__operational_system == 'windows':
            if platform.release() == '10':
                return 'windows-10'

            elif platform.release() == '11':
                return 'windows-11'

            return 'windows-7'

        elif self.__operational_system == 'mac':
            return 'mac'

        elif self.__operational_system == 'bsd':
            return 'bsd'

        return 'unknown'

    @staticmethod
    def __os() -> str:
        # 'unknown', 'linux', 'bsd', 'mac', 'windows'

        # Win config path: $HOME + AppData\Roaming\
        # Linux config path: $HOME + .config
        if os.name == 'posix':
            if platform.system() == 'Linux':
                return 'linux'

            elif platform.system() == 'Darwin':
                return 'mac'

        elif os.name == 'nt' and platform.system() == 'Windows':
            return 'windows'
