"""Solution to https://adventofcode.com/2015/day/23"""
import collections as c
import functools as ft
import itertools as it
import more_itertools as mit
import toolz
import utils.core as u


# Constants
Inst = c.namedtuple("Inst", ["inst", "arg1", "arg2"], defaults=[None])
State = c.namedtuple("State", ["a", "b", "next_inst"])

INIT_STATE = State(0, 0, 0)
INIT_STATE_B = State(1, 0, 0)


# Input parsing
def number_cast(s: str):
    """If the value is not the register string a or b, coerce to an int"""
    return int(s) if s not in {"a", "b"} else s


def parse_line(line: str):
    inst, rest = line.split(" ", 1)
    print(inst, rest)
    args = [number_cast(x) for x in rest.split(", ")]
    print(args)
    return Inst(inst, *args)


def parse(input):
    return [parse_line(line) for line in input]


# Puzzle logic
def jump_if_cond(state, arg1, arg2, cond):
    """Conditional jump-if. If the condition is satisfied on the current
    value of arg1, then jump to the index shifted by arg1. Otherwise,
    increment to the next instruction"""
    if cond(getattr(state, arg1)):
        return u.nt_update(state, {"next_inst": u.add(arg2)})
    else:
        return u.nt_update(state, {"next_inst": u.add(1)})


def next_state(instructions, state: State):
    """Selects the instruction recorded in the state's `next_inst`, and 
    returns the updated state using that instruction and its arguments"""
    inst, arg1, arg2 = instructions[state.next_inst]
    match inst:
        case "hlf": return u.nt_update(state, {arg1: lambda x: x//2,
                                               "next_inst": u.add(1)})

        case "tpl": return u.nt_update(state, {arg1: lambda x: x*3,
                                               "next_inst": u.add(1)})

        case "inc": return u.nt_update(state, {arg1: u.add(1),
                                               "next_inst": u.add(1)})

        case "jmp": return u.nt_update(state, {"next_inst": u.add(arg1)})

        case "jie": return jump_if_cond(state, arg1, arg2, lambda x: x % 2 == 0)

        case "jio": return jump_if_cond(state, arg1, arg2, lambda x: x == 1)


def isnotdone(max_inst, state: State):
    """Returns true if the program is not yet done, i.e. if the next
    instruction index is still within the bounds of the provided instructions"""
    return 0 <= state.next_inst < max_inst


def run_program(instructions, state: State) -> State:
    """Execute the logic in instructions against the starting state"""
    states = mit.iterate(ft.partial(next_state, instructions), state)
    return toolz.first(
        it.dropwhile(ft.partial(isnotdone, len(instructions)), states))


# Puzzle solutions
def part1(input):
    """The value in register b after running the program"""
    return run_program(input, INIT_STATE).b


def part2(input):
    """The value in register b after running the program with register a 
    starting at 1"""
    return run_program(input, INIT_STATE_B).b
