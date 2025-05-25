import copy
from hexlet_fs import get_children, get_meta, get_name, is_file, mkdir, mkfile


def downcase_file_names(tree):
    children = get_children(tree)

    def file_downcase(node):
        name = get_name(node)
        print(f'{name=}')
        if not is_file(node):
            return downcase_file_names(node)
        meta = get_meta(node)
        new_meta = copy.deepcopy(meta)
        new_name = name.lower()
        return mkfile(new_name, new_meta)
    
    new_children = map(file_downcase, children)
    new_meta = copy.deepcopy(get_meta(tree))
    return mkdir(get_name(tree), list(new_children), new_meta)


# BEGIN
def downcase_file_names_teacher(node):
    new_meta = copy.deepcopy(get_meta(node))
    name = get_name(node)
    if is_file(node):
        return mkfile(name.lower(), new_meta)
    children = get_children(node)
    new_children = map(downcase_file_names, children)
    return mkdir(name, list(new_children), new_meta)
# END

tree = mkdir('/', [
        mkdir('eTc', [
            mkdir('NgiNx', [], {'size': 4000}),
            mkdir(
                'CONSUL',
                [mkfile('config.JSON', {'uid': 0})],
            ),
        ]),
        mkfile('hOsts'),
    ])

print(downcase_file_names(tree))