import math
import pathlib
from time import time


def parse(puzzle_input):
    values = puzzle_input.split("\n")
    data = []
    for value in values[0].split():
        data.append(int(value))
    return data


def part1(data):
    new_data = {}
    for i in data:
        new_data[i] = 1
    result = calculate_amount(new_data, 25)
    return result


def calculate_amount(data, blinks):
    temp = data
    for i in range(0, blinks):
        data = temp
        temp = {}
        for value in data:
            if value == 0:
                temp[1] = temp.get(1, 0) + data[value]
            elif len(str(value)) % 2 == 0:
                stone_length = int(len(str(value)))
                one = int(str(value)[stone_length // 2:])
                two = int(str(value)[:stone_length // 2])
                temp[one] = temp.get(one, 0) + data[value]
                temp[two] = temp.get(two, 0) + data[value]
            else:
                temp[value * 2024] = temp.get(value * 2024, 0) + data[value]
    data = temp
    result_sum = 0
    for i in data:
        result_sum += data[i]
    return result_sum


def part2(data):
    new_data = {}
    for i in data:
        new_data[i] = 1
    result = calculate_amount(new_data, 75)
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
