import pathlib
from time import time


def parse(puzzle_input):
    values = puzzle_input.split("\n\n")
    updates = []
    order_rules = []
    for value in values[0].split("\n"):
        left, right = value.split("|")
        order_rules.append((int(left), int(right)))
    for value in values[1].split("\n"):
        ups = value.split(",")
        ups = [int(x) for x in ups]
        updates.append(ups)
    return updates, order_rules


def part1(updates, order_rules):
    result = 0
    for up in updates:
        if not breaks_rule(up, order_rules):
            result += up[len(up)//2]
    return result


def breaks_rule(update, order_rules):
    for rule in order_rules:
        if rule[0] in update and rule[1] in update:
            if not update.index(rule[0]) < update.index(rule[1]):
                return True
    return False


def part2(updates, order_rules):
    result = 0
    for up in updates:
        if breaks_rule(up, order_rules):
            new_up = change_order(up, order_rules)
            result += new_up[len(new_up)//2]
    return result


def change_order(update, order_rules):
    prev = 0
    changes = True
    while changes:
        for rule in order_rules:
            if rule[0] in update and rule[1] in update:
                i_0 = update.index(rule[0])
                i_1 = update.index(rule[1])
                if not i_0 < i_1:
                    update[i_0], update[i_1] = update[i_1], update[i_0]
                    prev = 1
        if prev == 0:
            changes = False
        prev = 0
    return update


def solve(puzzle_input):
    updates, order_rules = parse(puzzle_input)
    sol1 = part1(updates, order_rules)
    sol2 = part2(updates, order_rules)
    return sol1, sol2


def run():
    start_time = time()
    puzzle_input = pathlib.Path("input").read_text().strip()
    solutions = solve(puzzle_input)
    print(solutions)
    print("This took ", time() - start_time)

run()
