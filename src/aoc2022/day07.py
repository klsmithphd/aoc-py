"""Solution to https://adventofcode.com/2022/day/7"""
from functools import reduce
from more_itertools import flatten, split_before
from toolz import assoc_in, concatv
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


# Puzzle solutions

# day07_soln = \
#     AoCSolution(parse,
#                 p1=
#                 p2=)
