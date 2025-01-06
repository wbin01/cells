#!/usr/bin/env python3

def __replace_color(id_color, color, alpha, content) -> str:
    scopes = content.split('>')
    new_scopes = []
    for scope in scopes:
        if f'id="{id_color}"' in scope:

            new_props = []
            found_color = False
            found_alpha = False
            for prop in scope.split():

                if prop.startswith('fill="'):
                    prop = f'fill="{color}"'
                    found_color = True

                elif prop.startswith('fill-opacity="'):
                    prop = f'fill-opacity="{alpha}"' 
                    found_alpha = True
                    
                new_props.append(prop)

            if not found_color:
                new_props[1] = new_props[1] + f' fill="{color}"'

            if not found_alpha:
                new_props[1] = new_props[1] + f' fill-opacity="{alpha}"'


            new_scopes.append(' '.join(new_props))
        else:
            new_scopes.append(scope)

    break_mark = '-///*Bilbo_Baggins*///-'
    new_content = f'>{break_mark}'.join(new_scopes).replace('\n', '')
    return new_content.replace(break_mark, '\n')



if __name__ == '__main__':
    import pathlib
    import os


    path = (os.path.join(pathlib.Path(__file__).resolve().parent,
            'cells', 'core', 'static', 'radio.svg'))
    with open(path, 'r') as file_:
        content = file_.read()

    content = __replace_color('background', '#ff0000', '0.1', content)
    content = __replace_color('color', '#00ff00', '0.2', content)
    content = __replace_color('border', '#0000ff', '0.3', content)

    print('FINAL:\n------')
    print(content)
