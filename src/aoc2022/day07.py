"""Solution to https://adventofcode.com/2022/day/7"""
from functools import reduce
from more_itertools import split_before
from toolz import assoc_in, concatv
# from utils.core import AoCSolution

# Input parsing


def change_dir(state, dir):
    if (dir == '..'):
        newpath = state['path'][:-1]
        tree = state['tree']
    else:
        newpath = state['path'] + [dir]
        tree = assoc_in(state['tree'], newpath, {})
    return {'tree': tree, 'path': newpath}


def process_item(item: str):
    if (item.startswith("dir")):
        return (item[4:], {})
    else:
        size, name = item.split()
        return (name, int(size))


def list_dir(state, contents):
    return assoc_in(state, ['tree'] + state['path'], dict(process_item(x) for x in contents))


def process_cmd(state, cmd):
    if (cmd[0].startswith("$ cd")):
        return change_dir(state, cmd[0][5:])
    else:
        return list_dir(state, cmd[1:])


def parse(input):
    init_state = {'tree': {}, 'path': []}
    cmds = split_before(input, lambda s: s.startswith('$'))
    return reduce(process_cmd, cmds, init_state)['tree']


# Puzzle logic


# Puzzle solutions

# day07_soln = \
#     AoCSolution(parse,
#                 p1=
#                 p2=)
