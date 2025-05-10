#!/us/bin/env python3
import ast
import parso
from parso.python.tree import Class, Function
import pathlib
import re


class FindFiles(object):
    """FindFiles class"""
    def __init__(
        self, path_dirs: list, extensions: list, ignored_files: list) -> None:
        """FindFiles init"""
        self.__path_dirs = path_dirs
        self.__extensions = ['.' + x.lstrip('.').strip() for x in extensions]
        self.__ignored_files = ignored_files
        
        self.__files = []

    @property
    def extensions(self) -> list:
        """extensions doc"""
        return self.__extensions

    @extensions.setter
    def extensions(self, extensions: list) -> None:
        self.__update_files()
        self.__extensions = extensions

    @property
    def ignored_files(self) -> list:
        """ignored_files doc"""
        return self.__ignored_files

    @ignored_files.setter
    def ignored_files(self, ignored_files: list) -> None:
        self.__update_files()
        self.__ignored_files = ignored_files

    @property
    def path_dirs(self) -> list:
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
    """class doc"""
    def __init__(self, file_path: list):
        """init doc"""
        self.__file_path = file_path
        self.__scopes = {}
        self.num = 20
        self.cba = 'cba'

    def scopes(self) -> dict:
        """scope"""
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


class ClassParse():
    """Class parse"""

    def __init__(self, code_scope: str) -> None:
        """Class constructor"""
        self.__code_scope = code_scope
        self.__constructor_docstring = None
        self.__constructor_signature = None
        self.__docstring = None
        self.__inheritance = None
        self.__name = None
        self.__properties = None

    def constructor_docstring(self) -> str | None:
        """..."""
        if not self.__constructor_docstring:
            self.__constructor_docstring = self.__get_constructor_docstring()
        return self.__constructor_docstring

    def constructor_signature(self) -> str | None:
        """..."""
        if not self.__constructor_signature:
            self.__constructor_signature = self.__get_constructor_signature()
        return self.__constructor_signature

    def docstring(self) -> str | None:
        """..."""
        if not self.__docstring:
            self.__docstring = self.__get_docstring()
        return self.__docstring

    def inheritance(self) -> str | None:
        """..."""
        if not self.__inheritance:
            self.__name = self.__get_name_and_inheritance()
        return self.__inheritance

    def name(self) -> str | None:
        """..."""
        if not self.__name:
            self.__name = self.__get_name_and_inheritance()
        return self.__name

    def properties(self) -> dict | None:
        """..."""
        if not self.__properties:
            self.__properties = self.__get_properties()
        return self.__properties

    def __get_constructor_docstring(self) -> str | None:
        code = ' '.join(
            [x for x in self.__code_scope.split('def ') if '__init__' in x])
        init_doc = re.findall(
            r'__init__[^\"]+\"\"\"([^\"]+)|' "__init__[^\']+\'\'\'([^\']+)",
            code, re.DOTALL)

        return init_doc[0][0] or init_doc[0][1] if init_doc else None

    def __get_constructor_signature(self) -> str | None:
        init_sig = re.findall(r'__init__\([^\)]+\)[^:]+:',
            self.__code_scope, re.DOTALL)

        return init_sig[0] if init_sig else None

    def __get_docstring(self) -> str | None:
        code =  ' '.join(
            [x for x in self.__code_scope.split('def ') if 'class ' in x])
        class_doc = re.findall(
            r'class [^\"]+\"\"\"([^\"]+)|' "class [^\']+\'\'\'([^\']+)",
            code, re.DOTALL)

        return class_doc[0][0] or class_doc[0][1] if class_doc else None

    def __get_name_and_inheritance(self) -> str | None:
        name = re.findall(
            r'class ([^:]+):', self.__code_scope, re.DOTALL)[0].split('(')
        inher = name[1].replace(')', '').strip() if len(name) > 1 else None
        self.__inheritance = inher if inher else None

        return name[0] if name else None

    def __get_properties(self) -> dict:
        properties = {}

        funcs = self.__code_scope.split('def ')
        for prop in re.findall(
                r'@property[^\"]+\"\"\"[^\"]+\"\"\"',
                self.__code_scope, re.DOTALL):

            prop_name = re.findall(r'def ([^\(]+)\(', prop)
            prop_sig = re.findall(r'def ([^\:]+:)', prop)

            func = None
            for f in funcs:
                if f.startswith(prop_name[0]):
                    func = 'def ' + f
                    break

            prop_doc = None
            if func:
                p_doc = re.findall(
                    r'def [^\"]+\"\"\"([^\"]+)\"\"\"|'
                    "def [^\']+\'\'\'([^\']+)\'\'\'", func, re.DOTALL)
                prop_doc = p_doc[0][0] or p_doc[0][1] if p_doc else None

            properties[prop_name[0]] = {
                'signature': prop_sig[0] if prop_sig else None,
                'docstring': prop_doc if prop_doc else None}

        return properties


if __name__ == '__main__':
    import pprint
    BASE_DIR = pathlib.Path(__file__).resolve().parent.parent

    find_files = FindFiles(
        [BASE_DIR / 'cells'],
        ['py'],
        ['__init__.py'])
    # for item_file in find_files.file_paths():
    #     print(item_file)

    file_escopes = FileScopes(BASE_DIR / 'docs' / 'auto_dock.py')
    for k, v in file_escopes.scopes().items():
        if v.startswith('class'):
            cl = ClassParse(v)

            print('\nClass name:')
            print(f'    {cl.name()}')

            print('\nClass inheritance:')
            print(f'    {cl.inheritance()}')

            print('\nClass docstring:')
            print(f'    """{cl.docstring()}"""')

            print('\nClass constructor signature:')
            print(f'    {cl.constructor_signature()}')
            
            print('\nClass constructor docstring:')
            print(f'    """{cl.constructor_docstring()}"""')
            
            print('\nClass @property:')
            print('    ', end='')
            pprint.pprint(cl.properties())
            
            print('\nClass metods:')
        else:
            pass
            
        print('---')