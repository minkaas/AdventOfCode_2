import pathlib

def parse(puzzle_input):
    values = puzzle_input.split("\n")
    data = []
    calories = 0
    for value in values:
        if value == "":
            data.append(calories)
            calories = 0
        else:
            calories += int(value)
    return data


def part1(data):
    return max(data)


def part2(data):
    data.sort()
    return data.pop() + data.pop() + data.pop()

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
