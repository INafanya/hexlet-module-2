from hexlet_fs import get_children, get_name, is_file

def get_hidden_files_count(node):
    if is_file(node):
        name = get_name(node)
        if name.startswith('.'):
        return 1
    children = get_children(node)
    hidden_counts = list(map(get_hidden_files_count, children))
    return sum(hidden_counts)

[2, 
 [3, [4, [5, [6]]], [7]]
 ]