import pathlib
from time import time


def parse(puzzle_input):
    values = puzzle_input.split("\n")
    flipflops = {}
    conjunctions = {}
    broadcast = []
    for value in values:
        value = value.split(" -> ")
        if value[0] == "broadcaster":
            broadcast = value[1].split(", ")
        elif value[0][0] == "%":
            flipflops[value[0][1:]] = value[1].split(", ")
        elif value[0][0] == "&":
            conjunctions[value[0][1:]] = value[1].split(", ")
    return flipflops, conjunctions, broadcast


def part1(flipflops, conjunctions, broadcast):
    print(flipflops)
    print(conjunctions)
    print(broadcast)
    result = 0
    return result


def part2(flipflops, conjunctions, broadcast):
    result = 0
    return result


def solve(puzzle_input):
    flipflops, conjunctions, broadcast = parse(puzzle_input)
    sol1 = part1(flipflops, conjunctions, broadcast)
    sol2 = part2(flipflops, conjunctions, broadcast)
    return sol1, sol2


def run():
    start_time = time()
    puzzle_input = pathlib.Path("test").read_text().strip()
    solutions = solve(puzzle_input)
    print(solutions)
    print("This took ", time() - start_time)

run()
