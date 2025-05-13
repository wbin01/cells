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
        self.__files.sort()


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
        self.__methods = None
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

    def methods(self) -> str | None:
        if not self.__methods:
            self.__methods = self.__get_methods()
        return self.__methods if self.__methods else None

    def name(self) -> str | None:
        """..."""
        if not self.__name:
            self.__name = self.__get_name_and_inheritance()
        return self.__name

    def properties(self) -> dict | None:
        """..."""
        if not self.__properties:
            self.__properties = self.__get_properties()
        return self.__properties if self.__properties else None

    def __get_constructor_docstring(self) -> str | None:
        code = ' '.join(
            [x for x in self.__code_scope.split('def ') if '__init__' in x])
        init_doc = re.findall(
            r'__init__[^\"]+\"\"\"([^\"]+)|' "__init__[^\']+\'\'\'([^\']+)",
            code, re.DOTALL)

        return init_doc[0][0] or init_doc[0][1] if init_doc else None

    def __get_constructor_signature(self) -> str | None:
        # init_sig = re.findall(r'__init__\([^\)]+\)[^:]+:',
        init_sig = re.findall(r'__init__\([^\)]+\)[^\:]*:',
            self.__code_scope, re.DOTALL)

        return init_sig[0] if init_sig else None

    def __get_docstring(self) -> str | None:
        code =  ' '.join(
            [x for x in self.__code_scope.split('def ') if 'class ' in x])
        class_doc = re.findall(
            r'class [^\"]+\"\"\"([^\"]+)|' "class [^\']+\'\'\'([^\']+)",
            code, re.DOTALL)

        return class_doc[0][0] or class_doc[0][1] if class_doc else None

    def __get_methods(self) -> dict:
        if not self.__properties:
            self.__properties = self.__get_properties()

        methods = {}

        funcs = self.__code_scope.split('def ')
        for meth in re.findall(
                r'def [^\"]+\"\"\"[^\"]+\"\"\"',
                self.__code_scope, re.DOTALL):

            if meth.startswith('def __'):
                continue

            method_name = re.findall(r'def ([^\(]+)\(', meth)
            if method_name[0] in self.__properties:
                continue

            method_sig = re.findall(r'def ([^\)]+\)[^\:]*:)', meth)

            func = None
            for f in funcs:
                if f.startswith(method_name[0]):
                    func = 'def ' + f
                    break

            method_doc = None
            if func:
                m_doc = re.findall(
                    r'def [^\"]+\"\"\"([^\"]+)\"\"\"|'
                    "def [^\']+\'\'\'([^\']+)\'\'\'", func, re.DOTALL)
                method_doc = m_doc[0][0] or m_doc[0][1] if m_doc else None

            methods[method_name[0]] = {
                'signature': method_sig[0] if method_sig else None,
                'docstring': method_doc if method_doc else None}

        return methods

    def __get_name_and_inheritance(self) -> str | None:
        name = re.findall(
            r'class ([^:]+):', self.__code_scope, re.DOTALL)[0].split('(')
        inher = name[1].replace(')', '') if len(name) > 1 else None
        self.__inheritance = inher if inher else None

        if self.__inheritance == name[0]:
            self.__inheritance = 'object'

        return name[0] if name else None

    def __get_properties(self) -> dict:
        properties = {}

        funcs = self.__code_scope.split('def ')
        for prop in re.findall(
                r'@property[^\"]+\"\"\"[^\"]+\"\"\"',
                self.__code_scope, re.DOTALL):

            prop_name = re.findall(r'def ([^\(]+)\(', prop)
            prop_sig = re.findall(r'def ([^\)]+\)[^\:]*:)', prop)

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


class MdFiles(object):
    """..."""
    def __init__(
            self,
            files: FindFiles, documentation_path: str, mkdocs_yml_path: str
            ) -> None:
        """..."""
        self.__files = files
        self.__documentation_path = pathlib.Path(documentation_path)
        self.__yml_path = pathlib.Path(mkdocs_yml_path)

    def create_docs(self):
        yml_registry = []

        for file_path in self.__files.file_paths():
            file_scope = FileScopes(file_path)

            doc_content = '#  '
            scope_name = None
            scopes_found = 0

            for _, scope_content in file_scope.scopes().items():
                if scope_content.startswith('class'):
                    class_parse = ClassParse(scope_content)

                    if '# Internal control!' in class_parse.docstring():
                        continue

                    scopes_found += 1
                    scope_name, doc_content = self.__class_doc_content_parse(
                        class_parse, file_path)
                else:
                    # func_parse = FuncParse(scope_content)

                    # if '# Internal control!' in func_parse.docstring():
                    #     continue

                    # scopes_found += 1
                    # scope_name, doc_content = self.__func_doc_content_parse(
                    #     func_parse, file_path)
                    pass

            if scopes_found == 1:
                doc_content = doc_content.replace('#  ', '')

            doc_file_name = file_path.name.replace(file_path.suffix, '.md')

            with open(self.__documentation_path / doc_file_name,
                    'w', encoding='utf-8') as f:
                f.write(doc_content)
            
            yml_registry.append(
                (scope_name if scope_name else doc_file_name, doc_file_name))

        yml_content = (
            'site_name: Documentation\n'
            'site_url: https://wbin01.github.io/\n'
            'theme: readthedocs\n'
            'nav:\n'
            '    - Home: index.md\n')

        for item in yml_registry:
            yml_content += f'    - {item[0]}: {item[1]}\n'

        with open(self.__documentation_path / 'index.md', 'w',
                encoding='utf-8') as f:
            f.write('# INDEX')

        with open(self.__yml_path, 'w', encoding='utf-8') as f:
            f.write(yml_content)

    @staticmethod
    def __class_doc_content_parse(
            class_parse: ClassParse, file_path: pathlib) -> tuple:
        doc_content = '#  '
        scope_name = None

        if class_parse.name():
            doc_content += (
                '\n\n## <h2 style="color: #5697bf;">'
                f'<u>{class_parse.name()}</u>'
                '</h2>\n\n')

            if class_parse.name().lower() == file_path.name.replace(
                    file_path.suffix, ''):
                scope_name = class_parse.name()

        if class_parse.inheritance():
            doc_content += (
                '\n**Inherits from: '
                f'_{class_parse.inheritance()}_**\n')

        if class_parse.docstring():
            doc_content += f'\n{class_parse.docstring().replace(
                '    ', ' ')}\n'

        if class_parse.constructor_signature():
            doc_content += (
                '\n\n### <h2 style="color: #5e5d84;">Signature</h2>\n\n'
                '```python\n'
                f'{class_parse.constructor_signature()}\n'
                '```\n')
        
        if class_parse.constructor_docstring():
            text = class_parse.constructor_docstring().replace(
                '    ', ' ')

            for p in re.findall(r':param [^:]+:', text):
                text = re.sub(p, f'\n**{p}**', text)

            doc_content += f'\n{text}\n'

        if class_parse.properties():
            doc_content += (
                '\n\n### <h2 style="color: #5e5d84;">Properties</h2>\n\n')

            for prop_name, prop_value in class_parse.properties().items():
                doc_content += (
                    f'\n#### {prop_name}\n'
                    f'\n```python\n{prop_value['signature']}\n```\n')

                if prop_value['docstring']:
                    doc_content += f'\n{prop_value['docstring'].replace(
                        '    ', ' ')}\n'

        if class_parse.methods():
            doc_content += (
                '\n\n### <h2 style="color: #5e5d84;">Methods<h2>\n\n')

            for meth_name, meth_value in class_parse.methods().items():
                doc_content += (
                    f'\n#### {meth_name}\n'
                    f'\n```python\n{meth_value['signature']}\n```\n')

                if meth_value['docstring']:
                    doc_text = meth_value['docstring']
                    for p in re.findall(r':param [^:]+:', doc_text):
                        doc_text = re.sub(p, f'\n**{p}**', doc_text)

                    doc_content += f'\n{doc_text.replace(
                        '    ', ' ')}\n'

        return scope_name, doc_content


if __name__ == '__main__':
    import pprint
    BASE_DIR = pathlib.Path(__file__).resolve().parent.parent

    md = MdFiles(
        FindFiles(
            [BASE_DIR / 'cells'],
            ['py'],
            ['__init__.py', 'widgetbase.py']),
        BASE_DIR / 'docs',
        BASE_DIR / 'mkdocs.yml'
    )
    md.create_docs()