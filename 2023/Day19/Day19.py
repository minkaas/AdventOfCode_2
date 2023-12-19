import pathlib
from time import time
import re


def parse(puzzle_input):
    values = puzzle_input.split("\n\n")
    data = []
    rules = values[0].split("\n")
    ratings = []
    workflows = {}
    for rule in rules:
        workflow_name, flow = rule.split("{")
        workflows[workflow_name] = flow[:-1]
    for vals in values[1].split("\n"):
        parts = vals[1:-1:]
        parts = parts.split(",")
        to_add = []
        for part in parts:
            lett, num = part.split("=")
            to_add.append((lett, int(num)))
        ratings.append(to_add)
    for value in values:
        data.append(value)
    return workflows, ratings


def compare_with_part(part, comparison):
    part_name = comparison[0]
    value = int(comparison[2:])
    part_value = 0
    for par in part:
        if par[0] == part_name:
            part_value = par[1]
            break
    if '<' in comparison:
        return part_value < value
    elif '>' in comparison:
        return part_value > value


def check_acceptance(part, current_flow, workflows):
    to_check = workflows[current_flow]
    to_check = to_check.replace(':', ',').split(",")
    i = 0
    while i < len(to_check):
        if '<' in to_check[i] or '>' in to_check[i]:
            if compare_with_part(part, to_check[i]):
                i += 1
            else:
                i += 2
        elif to_check[i] == 'A':
            return True
        elif to_check[i] == 'R':
            return False
        else:
            new_flow = to_check[i]
            to_check = workflows[new_flow].replace(':', ',').split(",")
            i = 0


def part1(workflows, ratings):
    result = 0
    for part in ratings:
        if check_acceptance(part, "in", workflows):
            for letter, value in part:
                result += value
    return result


def part2(workflows, ratings):
    result = 0
    return result


def solve(puzzle_input):
    workflows, ratings = parse(puzzle_input)
    sol1 = part1(workflows, ratings)
    sol2 = part2(workflows, ratings)
    return sol1, sol2


def run():
    start_time = time()
    puzzle_input = pathlib.Path("input").read_text().strip()
    solutions = solve(puzzle_input)
    print(solutions)
    print("This took ", time() - start_time)

run()
