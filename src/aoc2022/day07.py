"""Solution to https://adventofcode.com/2022/day/7"""
from functools import cache, reduce
from more_itertools import flatten, split_before
from toolz import assoc_in, get_in
# from utils.core import AoCSolution

# Input parsing


def change_dir(state, dir):
    """
    Update `state` to reflect directory change
    """
    if (dir == '..'):
        newpath = state['path'][:-1]
        tree = state['tree']
    else:
        newpath = state['path'] + [dir]
        tree = assoc_in(state['tree'], newpath, {})
    return {'tree': tree, 'path': newpath}


def process_ls_item(item: str):
    """
    Return a tuple with the name of the item as the first element and
    the information about it as the second element. For a directory, the
    information is just an empty dict. For a file, the information is the
    file size.
    """
    if (item.startswith("dir")):
        return (item[4:], {})
    else:
        size, name = item.split()
        return (name, int(size))


def list_dir(state, contents):
    """
    Update `state` with the contents of the current directory
    """
    return assoc_in(state,
                    ['tree'] + state['path'],
                    dict(process_ls_item(x) for x in contents))


def process_cmd(state, cmd):
    """
    Update `state` based on the given `cmd`, either changing to a new directory 
    or adding the information provided by an `ls` command.
    """
    if (cmd[0].startswith("$ cd")):
        return change_dir(state, cmd[0][5:])
    else:
        return list_dir(state, cmd[1:])


def parse(input):
    init_state = {'tree': {}, 'path': []}
    cmds = split_before(input, lambda s: s.startswith('$'))
    return reduce(process_cmd, cmds, init_state)['tree']


# Puzzle logic

def dir_paths(tree, path=[]):
    """
    Returns a sequence of all the paths (nested key sequences) to the
    directories in `tree` 
    """
    for key, value in tree.items():
        if type(value) is dict:
            yield path+[key]
            for deeper_path in dir_paths(value, path+[key]):
                yield deeper_path


def dir_paths_alt(tree, path=[]):
    """
    Alternative implementation of `dir_paths`. Returns a list of all
    the paths (nested key sequences) to the directories in `tree`
    """
    return list(flatten([path+[k]] + dir_paths_alt(v, path+[k])
                        for k, v in tree.items() if type(v) is dict))


def node_size(tree, path):
    """
    Find the size of the node in the `tree` at location given by `path`.
    If the node represents a file, returns the size of the file. 
    If the node represents a directory, returns the sum of the size of all
    descendent nodes.
    """
    contents = get_in(path, tree)
    return contents if type(contents) is int else \
        sum(node_size(tree, path+[k]) for k in contents)


class MemoizedTreeSizer:
    """
    A memoized (cached) version of the `node_size` function.
    Python dicts are mutable, so they don't implement a hash function.
    All of the function arguments need to be hashable for the `@cache`
    decorator to work.

    This class closes over the `tree` argument and changes the signature
    to accept the path spread as args
    """

    def __init__(self, tree):
        self.tree = tree

    @cache
    def size(self, *path):
        contents = get_in(path, self.tree)
        return contents if type(contents) is int else \
            sum(self.size(*path, k) for k in contents)


# Puzzle solutions

# day07_soln = \
#     AoCSolution(parse,
#                 p1=
#                 p2=)
