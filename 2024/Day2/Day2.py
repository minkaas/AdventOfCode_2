import pathlib
from time import time


def parse(puzzle_input):
    values = puzzle_input.split("\n")
    data = []
    for value in values:
        intlist = []
        for val in value.split():
            intlist.append(int(val))
        data.append(intlist)
    return data


def safe_report(differences):
    if max(differences) > 3 or min(differences) < -3:
        return 0
    if differences.count(0) != 0:
        return 0
    if max(differences) > 0 and min(differences) < 0:
        return 0
    return 1


def part1(data):
    result = 0
    for report in data:
        differences = []
        for i in range(0, len(report) - 1):
            differences.append(report[i+1] - report[i])
        result += safe_report(differences)
    return result


def part2(data):
    result = 0
    for report in data:
        differences = []
        for i in range(0, len(report) - 1):
            differences.append(report[i + 1] - report[i])
        if safe_report(differences) == 1:
            result += 1
        else:
            for i in range(0, len(report)):
                differences = []
                new_report = report[:i] + report[i+1:]
                for j in range(0, len(new_report) - 1):
                    differences.append(new_report[j + 1] - new_report[j])
                if safe_report(differences):
                    result += 1
                    break
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
