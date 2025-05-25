import os

from hexlet_fs import flatten, get_children, get_name, is_file, mkdir, mkfile


# BEGIN (write your solution here)

    

def find_files_by_name(tree, text):
      
    def walk(node, ancestry):
        name = get_name(node)
        children = get_children(node)
        
        if is_file(node):
            if text in name:
                ancestry = os.path.join(ancestry, name)
                return ancestry
            return []
        output = list(
            map(
                lambda child: walk(child, os.path.join(ancestry, name)),
                children,
            )
        )
        return flatten(output)
    return walk(tree, '/')

# END

# BEGIN
def find_files_by_name_teacher(tree, substr):
    def walk(node, ancestry):
        name = get_name(node)
        new_ancestry = os.path.join(ancestry, name)
        if is_file(node):
            return [] if name.find(substr) < 0 else new_ancestry
        children = get_children(node)
        paths = map(lambda child: walk(child, new_ancestry), children)
        return flatten(paths)
    return walk(tree, '')
# END

tree = mkdir('/', [
        mkdir('etc', [
            mkdir('apache'),
            mkdir('nginx', [
                mkfile('nginx.conf', {'size': 800}),
            ]),
            mkdir('consul', [
                mkfile('config.json'),
                mkfile('data'),
                mkfile('raft'),
            ]),
        ]),
        mkfile('hosts', {'size': 3500}),
        mkfile('resolve', {'size': 1000}),
    ])

print(find_files_by_name(tree, 'co'))