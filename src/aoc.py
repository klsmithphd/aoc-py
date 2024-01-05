""" Runner for solutions to Advent of Code challenges """
from argparse import ArgumentParser
from importlib import import_module
from utils.core import input_path, puzzle_input, AoCSolution


def solution_module(year, day):
    return f"aoc{year}.day{day:02}"


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("year", type=int, help="Puzzle year")
    parser.add_argument("day", type=int, help="Puzzle day")
    parser.add_argument("-i", "--input", help="[Optional] puzzle input")
    parser.add_argument("-v", "--verbose", help="[Optional] verbose printing",
                        action='store_true')
    args = parser.parse_args()

    filename = args.input if args.input else input_path(args.year, args.day)
    input = puzzle_input(filename)

    soln_mod = import_module(solution_module(args.year, args.day))
    soln = AoCSolution(soln_mod.parse, soln_mod.part1, soln_mod.part2)

    if (args.verbose):
        print(f"Advent of Code {args.year}, Day {args.day}, using {filename}")
        print()
        print("Part 1 solution:")
        print(soln.part1_doc())
    print(soln.part1(input))
    if (args.verbose):
        print()
        print("Part 2 solution:")
        print(soln.part2_doc())
    print(soln.part2(input))
