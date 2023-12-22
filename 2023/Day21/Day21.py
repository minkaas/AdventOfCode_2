import pathlib
from time import time


def parse(puzzle_input):
    values = puzzle_input.split("\n")
    data = []
    start = (0, 0)
    x = 0
    for value in values:
        to_add = []
        for i in range(len(value)):
            if value[i] == 'S':
                to_add.append(False)
                start = (x, i)
            elif value[i] == '.':
                to_add.append(False)
            else:
                to_add.append(True)
        data.append(to_add)
        x += 1
    return data, start


def print_matrix(data):
    for dat in data:
        to_print = ""
        for da in dat:
            if da:
                to_print += "#"
            else:
                to_print += "."
        print(to_print)


def part1(data, start):
    print(start)
    print_matrix(data)
    result = 0
    return result


def part2(data):
    result = 0
    return result


def solve(puzzle_input):
    data, start = parse(puzzle_input)
    sol1 = part1(data, start)
    sol2 = part2(data)
    return sol1, sol2


def run():
    start_time = time()
    puzzle_input = pathlib.Path("test").read_text().strip()
    solutions = solve(puzzle_input)
    print(solutions)
    print("This took ", time() - start_time)

run()
