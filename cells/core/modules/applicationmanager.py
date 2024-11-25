#!/usr/bin/env python3
import os
import logging

from .platform import Platform


class ApplicationManager(object):
    """Dev mode integration

    Temporary integration with the platform when in development mode
    """

    def __init__(self, *args, **kwargs) -> None:
        """Class constructor"""
        self.__args = args[0][0]

        self.__platform = Platform()
        self.__frame_id = None
        self.__filename_ext = None
        self.__filename = None
        self.__wm_class = None
        self.__app_name = None
        self.__work_dir = None
        self.__icon = None

        # Linux
        self.__linux_icon_has_set = False
        self.__linux_applications_dir = None
        self.__linux_desktop_file_url = None

    @property
    def frame_id(self) -> list:
        """Frame identity list

        List containing app identity information.
        The first item is the main file, __file__, followed by an ID
        Example:
            [__file__, 'app_id', 'App Name']

        When set the list, all items are optional, but the order is mandatory
        """
        return self.__frame_id

    @frame_id.setter
    def frame_id(self, frame_id: list) -> None:
        # General
        self.__frame_id = frame_id
        self.__filename_ext = '.' + frame_id[0].split('/')[-1].split('.')[-1]
        self.__filename = frame_id[0].split('/')[-1].rstrip(self.__filename_ext)
        self.__wm_class = self.__filename if len(frame_id) < 2 else frame_id[1]
        self.__app_name = self.__wm_class if len(frame_id) < 3 else frame_id[2]
        self.__work_dir = os.path.dirname(frame_id[0])

        # Linux
        self.__linux_applications_dir = os.path.join(
                os.environ['HOME'], '.local', 'share', 'applications')
        self.__linux_desktop_file_url = os.path.join(
                self.__linux_applications_dir, self.__wm_class + '.desktop')
        self.__linux_wayland_tmp_desktop_for_icon()

    @property
    def icon(self) -> str:
        """Frame icon path string

        Application Icon
        """
        return self.__icon

    @icon.setter
    def icon(self, path: str) -> None:
        """Frame icon path string

        Application Icon
        """
        self.__icon = path
        self.__linux_wayland_tmp_desktop_for_icon()

    @property
    def wm_class(self) -> str:
        """Window Manager Class

        Application ID
        """
        return self.__wm_class

    @wm_class.setter
    def wm_class(self, wm_class: str) -> None:
        self.__wm_class = wm_class

    def clear_tmp(self):
        """Clear temp configs"""
        if not '--dev' in self.__args:
            return
        
        if os.path.isfile(self.__linux_desktop_file_url):
            os.remove(self.__linux_desktop_file_url)

    def __linux_wayland_tmp_desktop_for_icon(self) -> None:
        # BASEDIR=$(dirname $0)
        # echo "Script on ${BASEDIR}"

        if not '--dev' in self.__args:
            return
        if not self.__icon:
            return
        if self.__linux_icon_has_set:
            return

        if self.__platform.operational_system == 'linux' and self.__frame_id:
            with open(self.__linux_desktop_file_url, 'w') as f:
                f.write(
                    '[Desktop Entry]\n'
                    f'Name={self.__app_name}\n'
                    f'Exec={self.__frame_id[0]}\n'
                    f'Icon={self.__icon}\n'
                    'PrefersNonDefaultGPU=false\n'
                    'StartupNotify=true\n'
                    'Terminal=false\n'
                    'Type=Application\n'
                    'X-KDE-SubstituteUID=false\n')

            os.chmod(self.__frame_id[0] , 0o777)
            self.__linux_icon_has_set = True
