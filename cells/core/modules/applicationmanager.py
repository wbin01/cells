#!/usr/bin/env python3
import logging
import os
import string
import sys

from .platformselector import PlatformSelector


class ApplicationManager(object):
    """Dev mode integration

    Temporary integration with the platform when in development mode
    """

    def __init__(self, *args, **kwargs) -> None:
        """Class constructor"""
        self.__args = args[0][0]
        self.__path = os.path.dirname(os.path.abspath(__file__))

        self.__platform = PlatformSelector()
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
        self.__linux_desktop_file_url_root = None
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

        self.__check__wm_class()

        # Linux
        self.__linux_applications_dir = os.path.join(
                os.environ['HOME'], '.local', 'share', 'applications')
        self.__linux_desktop_file_url = os.path.join(
                self.__linux_applications_dir, self.__wm_class + '.desktop')
        self.__linux_desktop_file_url_root = os.path.join(
            '/usr/share/applications', self.__wm_class + '.desktop')
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
        if self.__platform.operational_system == 'linux' and self.__frame_id:
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
        if os.path.isfile(self.__linux_desktop_file_url):
            os.remove(self.__linux_desktop_file_url)

    def __linux_wayland_tmp_desktop_for_icon(self) -> None:
        # BASEDIR=$(dirname $0)
        # echo "Script on ${BASEDIR}"
        if not self.__icon or self.__linux_icon_has_set:
            return

        if (not os.path.isfile(self.__linux_desktop_file_url) or not
                os.path.isfile(self.__linux_desktop_file_url_root)):

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

    def __check__wm_class(self):
        message = (
            '\nID name must be 3 characters or more, and can only contain '
            'lowercase letters, numbers or underscores "_", such as:\n'
            '    [__file__, "\033[0;34mapp_4_me\033[0m", "App 4 me" ]\n')

        if len(self.__wm_class) < 3:
            print(message)
            sys.exit(-1)

        for char in self.__wm_class:
            if char not in string.ascii_lowercase + string.digits + '_':
                print(message)
                sys.exit(-1)

    def deploy(self) -> None:
        if not self.__frame_id or not self.__icon:
            print(
                '\n | First set the "\033[0;34mframe_id\033[0m" and '
                '"\033[0;34micon\033[0m" properties of\n | the '
                'application. Example:\n |\n'
                ' |   app = Application(sys.argv)\n'
                ' |   app.frame = MainFrame()\n'
                ' |\033[0;34m   app.frame_id = [__file__, "my_app", "My App"]'
                ' |\033[0m\n'
                ' |\033[0;34m   app.icon = "/path/to/my/icon.svg"'
                ' |\033[0m\n'
                ' |   app.exec()\n')
            sys.exit(-1)

        if self.__platform.operational_system == 'linux' and self.__frame_id:
            static_files_path = self.__deploy_linux_collect_static_files()
            scripts_path = self.__deploy_linux_collect_scripts()
            desktop_file_path = self.__deploy_linux_create_desktop_file()

            applications_path = os.path.join('usr', 'share', 'applications')
            icon_path = os.path.join(
                'usr', 'share', 'icons', 'hicolor', '48x48', 'apps')

        # TODO: message about application
        print('deployment completed!')

    def __deploy_linux_collect_static_files(self) -> str:
        pass

    def __deploy_linux_collect_scripts(self) -> str:
        pass

    def __deploy_linux_create_desktop_file(self) -> str:
        # TODOs | Exec and Icon as self.__wm_class
        generic_name = ''
        comment = ''
        app_type = 'Application'
        categories = 'Utility;'
        terminal = 'false'
        terminal_opt = ''
        mime = ''

        # TODO: Copy and rename icon to self.__wm_class

        desktop_path = os.path.join(
            self.__work_dir, self.__wm_class + '.desktop')

        with open(desktop_path, 'w') as f:
            f.write(
                '[Desktop Entry]\n'
                f'Name={self.__app_name}\n'
                f'GenericName={generic_name}\n'
                f'Comment={comment}\n'
                f'Exec={self.__wm_class}\n'
                f'Icon={self.__wm_class}\n'
                f'Type={app_type}\n'
                f'Categories={categories}\n'
                f'Terminal={terminal}\n'
                f'TerminalOptions={terminal_opt}\n'
                f'MimeType={mime}\n'
                f'StartupNotify=true\n'
                f'X-KDE-SubstituteUID=false\n'
                f'PrefersNonDefaultGPU=false\n')

        os.chmod(desktop_path , 0o777)
        return desktop_path
