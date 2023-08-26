""" Runner for solutions to Advent of Code challenges """
from argparse import ArgumentParser
from utils.core import input_path, puzzle_input
import aoc2022

solutions = {
    2022: aoc2022.solutions
}

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

    soln = solutions[args.year][args.day]
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
