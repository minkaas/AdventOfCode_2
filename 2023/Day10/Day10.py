import pathlib


def parse(puzzle_input):
    values = puzzle_input.split("\n")
    data = []
    for value in values:
        data.append(value)
    return data


def part1(data):
    result = 0
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
    puzzle_input = pathlib.Path("input").read_text().strip()
    solutions = solve(puzzle_input)
    print(solutions)


run()
