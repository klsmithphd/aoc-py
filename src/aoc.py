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
    parser.add_argument("--input", help="[Optional] puzzle input")
    args = parser.parse_args()

    filename = args.input if args.input else input_path(args.year, args.day)
    input = puzzle_input(filename)

    soln1, soln2 = solutions[args.year][args.day]
    print(f"Advent of Code {args.year}, Day {args.day}, using {filename}")
    print(f"Part 1 solution: {soln1(input)}")
    print(f"Part 2 solution: {soln2(input)}")
