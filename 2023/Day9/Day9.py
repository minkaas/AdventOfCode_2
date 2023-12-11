import pathlib
from time import time


def parse(puzzle_input):
    values = puzzle_input.split("\n")
    data = []
    for value in values:
        res = []
        for num in value.split(" "):
            res.append(int(num))
        data.append(res)
    return data


def get_history(history):
    result = 0
    new_history = []
    for i in range(0, len(history) - 1):
        one, two = history[i], history[i + 1]
        new_history.append(two - one)
    if any(new_history):
        result += get_history(new_history)
    result += history[-1]
    return result


def part1(data):
    result = 0
    for history in data:
        result += get_history(history)
    return result


def part2(data):
    result = 0
    for history in data:
        result += get_backwards_history(history)
    return result


def get_backwards_history(history):
    result = 0
    new_history = []
    for i in range(0, len(history) - 1):
        one, two = history[i], history[i + 1]
        new_history.append(two - one)
    if any(new_history):
        result += get_backwards_history(new_history)
    result = history[0] - result
    return result


def solve(puzzle_input):
    data = parse(puzzle_input)
    sol1 = part1(data)
    sol2 = part2(data)
    return sol1, sol2


def run():
    start_time = time()
    puzzle_input = pathlib.Path("input").read_text().strip()
    solutions = solve(puzzle_input)
    print(solutions)
    print("This took ", time() - start_time)


run()
