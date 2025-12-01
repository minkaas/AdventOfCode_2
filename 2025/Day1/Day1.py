import pathlib
from time import time


def parse(puzzle_input):
    values = puzzle_input.split("\n")
    data = []
    for value in values:
        data.append(value)
    return data


def part1(data):
    result = 50
    final = 0
    for point in data:
        if 'R' in point:
            result += int(point[1:])
            result %= 100
        else:
            result -= int(point[1:])
            result += 100
            result %= 100
        if result == 0:
            final += 1
    return final


def part2(data):
    result = 50
    final = 0
    for point in data:
        if 'R' in point:
            for i in range(0, int(point[1:])):
                result += 1
                result %= 100
                if result == 0:
                    final += 1
        else:
            for i in range(0, int(point[1:])):
                result -= 1
                result += 100
                result %= 100
                if result == 0:
                    final += 1
    return final

def solve(puzzle_input):
    data = parse(puzzle_input)
    sol1 = part1(data)
    data = parse(puzzle_input)
    sol2 = part2(data)
    return sol1, sol2


def run():
    start_time = time()
    puzzle_input = pathlib.Path("input").read_text().strip()
    solutions = solve(puzzle_input)
    print(solutions)
    print("This took ", time() - start_time)

run()
