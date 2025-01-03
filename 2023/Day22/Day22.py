import pathlib
from time import time


def parse(puzzle_input):
    values = puzzle_input.split("\n")
    data = []
    for value in values:
        value = value.split("~")
        start = value[0].split(",")
        end = value[1].split(",")
        data.append((start, end))
    return data


def part1(data):
    result = 0
    brick_map = [[[]]]
    print(data)
    for brick in data:
        start, end = brick
        x, y, z = start
        x1, y1, z1 = end


    return result


def part2(data):
    result = 0
    return result


def solve(puzzle_input):
    data = parse(puzzle_input)
    sol1 = part1(data)
    sol2 = part2(data)
    return sol1, sol2


def run():
    start_time = time()
    puzzle_input = pathlib.Path("test").read_text().strip()
    solutions = solve(puzzle_input)
    print(solutions)
    print("This took ", time() - start_time)

run()
