from itertools import chain

def remove_first_level(tree_list: list) -> list:
    result = []
    for elem in tree_list:
        if isinstance(elem, list):
            for item in elem:
                result.append(item)
    return result


def remove_first_level(tree):
    children = filter(lambda item: isinstance(item, list), tree)
    return list(chain(*children))