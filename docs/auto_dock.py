#!/us/bin/env python3
import ast
import pathlib



class FindFiles(object):
    """"""
    def __init__(
        self, path_dirs: list, extensions: list, ignored_files: list) -> None:
        """"""
        self.__path_dirs = path_dirs
        self.__extensions = ['.' + x.lstrip('.').strip() for x in extensions]
        self.__ignored_files = ignored_files
        
        self.__files = []

    @property
    def extensions(self) -> list:
        """..."""
        return self.__extensions

    @extensions.setter
    def extensions(self, extensions: list) -> None:
        self.__update_files()
        self.__extensions = extensions

    @property
    def ignored_files(self) -> list:
        """..."""
        return self.__ignored_files

    @ignored_files.setter
    def ignored_files(self, ignored_files: list) -> None:
        self.__update_files()
        self.__ignored_files = ignored_files

    @property
    def path_dirs(self) -> list:
        """..."""
        return self.__path_dirs

    @path_dirs.setter
    def path_dirs(self, path_dirs: list) -> None:
        self.__update_files()
        self.__path_dirs = path_dirs

    def file_paths(self) -> list:
        """..."""
        if not self.__files:
            self.__update_files()
        return self.__files

    def __update_files(self) -> None:
        for path in self.__path_dirs:
            for item_file in pathlib.Path(path).iterdir():

                if item_file.suffix in self.__extensions:
                    if item_file.name not in self.__ignored_files:
                        self.__files.append(item_file)


class FileScopes(object):
    """..."""
    def __init__(self, file_path: list):
        self.__file_path = file_path
        self.__scopes = {}

    def scopes(self) -> dict:
        """..."""
        if not self.__scopes:
            self.__extract_scopes()
        return self.__scopes

    def __extract_scopes(self):
        lines = pathlib.Path(self.__file_path).read_text().splitlines()
        tree = ast.parse("\n".join(lines))

        for node in ast.iter_child_nodes(tree):
            if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
                scope_start = node.lineno - 1
                scope_end = getattr(node, 'end_lineno', None)
                if scope_end is None:
                    # Fallback Python < 3.8: pegar até próxima definição ou EOF
                    scope_end = scope_start + 1
                    while scope_end < len(lines) and not lines[
                            scope_end].lstrip().startswith(("def ", "class ")):
                        scope_end += 1
                
                node_block = lines[scope_start:scope_end]

                self.__scopes[
                    'class ' + node.name if isinstance(
                        node, ast.ClassDef) else 'def ' + node.name
                    ] = "\n".join(node_block)


if __name__ == '__main__':
    BASE_DIR = pathlib.Path(__file__).resolve().parent.parent

    find_files = FindFiles(
        [BASE_DIR / 'cells'],
        ['py'],
        ['__init__.py'])
    # for item_file in find_files.file_paths():
    #     print(item_file)

    file_escopes = FileScopes(BASE_DIR / 'docs' / 'auto_dock.py')
    # for k, v in file_escopes.scopes().items():
    #     print(k)
    #     print(v)
    #     print('-----')
