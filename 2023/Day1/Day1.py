import pathlib
from time import time


def parse(puzzle_input):
    values = puzzle_input.split("\n")
    data = []
    for value in values:
        data.append(value)
    return data


def get_first_and_last_dig(calibration_line):
    digits = [(i, int(digit)) for i, digit in enumerate(calibration_line) if digit.isdigit()]
    return digits[0][1], digits[-1][1]


def part1(data):
    result = 0
    for value in data:
        num1, num2 = get_first_and_last_dig(value)
        result += int(num1) * 10 + int(num2)
    return result


def part2(data):
    result = 0
    for value in data:
        value = replace_written(value)
        num1, num2 = get_first_and_last_dig(value)
        result += int(num1) * 10 + int(num2)
    return result


def replace_written(cal_line):
    result = cal_line
    result = result.replace("one", "o1ne")
    result = result.replace("two", "t2wo")
    result = result.replace("three", "th3ree")
    result = result.replace("four", "fo4ur")
    result = result.replace("five", "fi5ve")
    result = result.replace("six", "s6ix")
    result = result.replace("seven", "se7ven")
    result = result.replace("eight", "ei8ght")
    result = result.replace("nine", "ni9ne")
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
