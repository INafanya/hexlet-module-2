from hexlet_fs import mkdir, mkfile, get_children, get_meta, get_name, is_file


# BEGIN (write your solution here)
def du(tree):
    def get_file_size(node):
        meta = get_meta(node)
        if is_file(node):
            return meta['size']

        children = get_children(node)
        sizes = list(map(get_file_size, children))
        return sum(sizes)

    children = get_children(tree)
    result = list(map(
        lambda child: (get_name(child), get_file_size(child)),
        children,
    ))
    print(result)
    return (sorted(result, key=lambda size: result[1], reverse = True))

# END

def calculate_entry_size(tree):
    if is_file(tree):
        meta = get_meta(tree)
        return meta['size']
    children = get_children(tree)
    sizes = list(map(calculate_entry_size, children))
    return sum(sizes)


def du_tescher(tree):
    children = get_children(tree)
    result = list(map(
        lambda child: (get_name(child), calculate_entry_size(child)),
        children,
    ))
    result.sort(key=lambda entry: entry[1], reverse=True)
    return result

tree_1 = mkdir('/', [
        mkdir('etc', [
            mkdir('apache'),
            mkdir('nginx', [
                mkfile('nginx.conf', {'size': 800}),
            ]),
            mkdir('consul', [
                mkfile('.config.json', {'size': 1200}),
                mkfile('data', {'size': 8200}),
                mkfile('raft', {'size': 80}),
            ]),
        ]),
        mkfile('hosts', {'size': 3500}),
        mkfile('resolve', {'size': 1000}),
    ])
# [('etc', 10280), ('hosts', 3500), ('resolve', 1000)]

print(du(tree_1))
print(du_tescher(tree_1))