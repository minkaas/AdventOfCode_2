import pathlib
from time import time


def parse(puzzle_input):
    values = puzzle_input.split("\n")
    data = []
    for value in values:
        data.append(int(value))
    return data


def part1(data):
    result = 0
    for battery in data:
        battery = [int(d) for d in str(battery)]
        max_digit = max(battery)
        if battery.index(max_digit) < len(battery) - 1:
            first_digit = max_digit
            remaining_battery = battery[battery.index(max_digit)+1:len(battery)]
            second_digit = max(remaining_battery)
            result += 10* first_digit + second_digit
        else:
            max_digit = max(battery[0:-1])
            first_digit = max_digit
            remaining_battery = battery[battery.index(max_digit)+1:len(battery)]
            second_digit = max(remaining_battery)
            result += 10 * first_digit + second_digit
    return result


def part2(data):
    result = 0
    for battery in data:
        battery = [int(d) for d in str(battery)]
        joltage = ""
        for i in range(0, 11):
            max_digit = max(battery[0:-11+i])
            joltage += str(max_digit)
            battery = battery[battery.index(max_digit)+1:len(battery)]
        joltage += str(max(battery))
        result += int(joltage)
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