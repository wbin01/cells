#!/usr/bin/env python3


class IniParse(object):
    """..."""
    def __init__(self):
        self.__url = '/home/user/Dev/github/cells/cells/core/modules/static/stylerc'
        self.__content = None
        self.__parse_file_to_dict()

    def content(self):
        return self.__content
    
    def __parse_file_to_dict(self, url) -> None:
        with open(url, 'r') as ini_file:
            ini_text = ini_file.read()

        content = {}
        for scope in ini_text.split('['):
            if not scope.strip().startswith('#'):
                scope = f'[{scope.strip()}'

            header, key, value = '', '', ''
            for line in scope.split('\n'):
                if line and not line.strip().startswith('#'):
                    line = line.strip()

                    if line.startswith('['):
                        header = line
                        content[header] = {}

                    elif '=' in line:
                        key, value = line.split('=')
                        content[header][key] = value

                    else:
                        value = content[header][key] + line
                        content[header][key] = value

        return content


if __name__ == '__main__':
    import pprint

    ini = IniParse()
    pprint.pprint(ini.content())
