import pathlib
import re
import numpy as np
from time import time


def parse(puzzle_input):
    values = puzzle_input.split("\n")
    data = []
    operators = []
    for value in values[:-1]:
        temp = []
        for val in value.split():
            temp.append(int(val))
        data.append(temp)
    for val in values[-1].split():
        operators.append(val)
    return data, operators, values


def part1(data, operators):
    result = 0
    for i in range(0, len(data[0])):
        equation = ""
        for j in range(0, len(data) - 1):
            equation += str(data[j][i]) + operators[i]
        equation += str(data[len(data) - 1][i])
        result += eval(equation)
    return result


def part2(data, operators, values):
    result = 0
    current = 0
    for i in range(0, len(data[0])):
        equation = ""
        nums = []
        for j in range(0, len(data)):
            nums.append(data[j][i])
        to_take = len(str(max(nums)))
        number_matrix = []
        for value in values[:-1]:
            number_matrix.append(value[current:current + to_take+1])
        new_nums = []
        for k in range(0, to_take):
            new_num = ""
            for j in range(0, len(number_matrix)):
                new_num += number_matrix[j][k]
            new_nums.append(new_num)
        for num in new_nums[:-1]:
            equation += num + operators[i]
        equation += new_nums[-1]
        result += eval(equation)
        current += to_take + 1
    return result


def create_new_nums(nums):
    result = []

    return result


def solve(puzzle_input):
    data, operators, values = parse(puzzle_input)
    sol1 = part1(data, operators)
    data, operators, values = parse(puzzle_input)
    sol2 = part2(data, operators, values)
    return sol1, sol2


def run():
    start_time = time()
    puzzle_input = pathlib.Path("input").read_text().strip()
    solutions = solve(puzzle_input)
    print(solutions)
    print("This took ", time() - start_time)

run()