import pathlib
from time import time


def parse(puzzle_input):
    values = puzzle_input.split("\n")
    left_list = []
    right_list = []
    for value in values:
        lr = value.split()
        left_list.append(int(lr[0]))
        right_list.append(int(lr[1]))
    return left_list, right_list


def part1(left_list, right_list):
    left_list.sort()
    right_list.sort()
    result = 0
    for i in range(0, len(left_list)):
        result += abs(left_list[i] - right_list[i])
    return result


def part2(left_list, right_list):
    result = 0
    for i in left_list:
        result += i * right_list.count(i)
    return result


def solve(puzzle_input):
    left_list, right_list = parse(puzzle_input)
    sol1 = part1(left_list, right_list)
    sol2 = part2(left_list, right_list)
    return sol1, sol2


def run():
    start_time = time()
    puzzle_input = pathlib.Path("input").read_text().strip()
    solutions = solve(puzzle_input)
    print(solutions)
    print("This took ", time() - start_time)

run()
