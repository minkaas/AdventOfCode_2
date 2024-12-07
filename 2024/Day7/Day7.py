import pathlib
from time import time


def parse(puzzle_input):
    values = puzzle_input.split("\n")
    data = []
    for value in values:
        val = value.split(": ")
        temp = []
        temp.append(int(val[0]))
        for v in val[1].split(" "):
            temp.append(int(v))
        data.append(temp)
    return data


def add_func(test_val, equation, part2=False):
    current = equation[0]
    equation = equation[1:]
    if current == test_val and len(equation) == 0:
        return True
    if len(equation) == 0:
        return False
    if current > test_val:
        return False
    equation[0] += current
    if current > test_val:
        return False
    if part2:
        return add_func(test_val, equation, True) | mult_func(test_val, equation, True) | conc_func(test_val, equation)
    return add_func(test_val, equation) | mult_func(test_val, equation)


def mult_func(test_val, equation, part2=False):
    current = equation[0]
    equation = equation[1:]
    if current == test_val and len(equation) == 0:
        return True
    if len(equation) == 0:
        return False
    equation[0] *= current
    if current > test_val:
        return False
    if part2:
        return add_func(test_val, equation, True) | mult_func(test_val, equation, True) | conc_func(test_val, equation)
    return add_func(test_val, equation) | mult_func(test_val, equation)


def can_make(calib, part2=False):
    test_val = calib.pop(0)
    if part2:
        return add_func(test_val, calib, True) | mult_func(test_val, calib, True) | conc_func(test_val, calib)
    return add_func(test_val, calib) | mult_func(test_val, calib)


def part1(data):
    result = 0
    for calibration in data:
        to_add = calibration[0]
        if can_make(calibration):
            result += to_add
    return result


def conc_func(test_val, equation):
    current = equation[0]
    equation = equation[1:]
    if current == test_val and len(equation) == 0:
        return True
    if len(equation) == 0:
        return False
    equation[0] = int(str(current) + str(equation[0]))
    if current > test_val:
        return False
    return add_func(test_val, equation, True) | mult_func(test_val, equation, True) | conc_func(test_val, equation)



def part2(data):
    result = 0
    for calibration in data:
        to_add = calibration[0]
        if can_make(calibration, True):
            result += to_add
    return result


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
