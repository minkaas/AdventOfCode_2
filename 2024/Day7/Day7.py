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


def addv(current, equation, i, part_2=False):
    if current > equation[0]:
        return False
    if i == len(equation) and current == equation[0]:
        return True
    elif i == len(equation):
        return False
    new_current = current + equation[i]
    if part_2:
        return addv(new_current, equation, i + 1, True) or multv(new_current, equation, i + 1, True) or concv(new_current, equation, i+1)
    return addv(new_current, equation, i+1) or multv(new_current, equation, i+1)


def multv(current, equation, i, part_2=False):
    if current > equation[0]:
        return False
    if i == len(equation) and current == equation[0]:
        return True
    elif i == len(equation):
        return False
    new_current = current * equation[i]
    if part_2:
        return addv(new_current, equation, i + 1, True) or multv(new_current, equation, i + 1, True) or concv(new_current, equation, i+1)
    return addv(new_current, equation, i+1) or multv(new_current, equation, i+1)


def part1(data):
    result = 0
    for calibration in data:
        if addv(calibration[1], calibration, 2) or multv(calibration[1], calibration, 2):
            result += calibration[0]
    return result


def concv(current, equation, i):
    if current > equation[0]:
        return False
    if i == len(equation) and current == equation[0]:
        return True
    elif i == len(equation):
        return False
    new_current = int(str(current) + str(equation[i]))
    return addv(new_current, equation, i + 1, True) or multv(new_current, equation, i + 1, True) or concv(new_current, equation, i+1)


def part2(data):
    result = 0
    for calibration in data:
        if addv(calibration[1], calibration, 2, True) or multv(calibration[1], calibration, 2, True) or concv(calibration[1], calibration, 2):
            result += calibration[0]
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
