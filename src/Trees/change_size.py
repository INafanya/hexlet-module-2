import copy

from hexlet_fs import get_children, get_meta, get_name, is_file, mkdir, mkfile


# BEGIN (write your solution here)
def compress_images(tree):
    def check_children(node):
        new_meta = copy.deepcopy(get_meta(node))
        if is_file(node):
            if 'jpg' in get_name(node).split('.'):
                new_meta['size'] = new_meta['size'] / 2
                return mkfile(get_name(node), new_meta)
            return mkfile(get_name(node), new_meta)
        return mkdir(get_name(node), get_children(node), new_meta)

    children = get_children(tree)
    new_children = list(map(check_children, children))
    new_meta = copy.deepcopy(get_meta(tree))
    new_tree = mkdir(get_name(tree), new_children, new_meta)
    return new_tree
# END

# BEGIN
def compress_images_teacher(tree):
    children = get_children(tree)

    def reduce_image_size(node):
        name = get_name(node)
        if not is_file(node) or not name.endswith('.jpg'):
            return node
        meta = get_meta(node)
        new_meta = copy.deepcopy(meta)
        new_meta['size'] //= 2
        return mkfile(name, new_meta)

    new_children = map(reduce_image_size, children)
    new_meta = copy.deepcopy(get_meta(tree))
    return mkdir(get_name(tree), list(new_children), new_meta)
# END

# node = mkfile('test.jpg', meta={'type': 'file'})
# print(get_name(node).split('.'))

tree_test1 = mkdir('documents', [
        mkdir('presentations'),
    ])

print(compress_images(tree_test1))