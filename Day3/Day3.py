import pathlib
import string


def parse(puzzle_input):
    values = puzzle_input.split("\n")
    data = []
    result = []
    i = 0
    for value in values:
        result.append(value)

    for value in values:
        firstpart, secondpart = value[:len(value) // 2], value[len(value) // 2:]
        data.append([firstpart, secondpart])
    return data, result


def part1(data):
    priority = 0
    for rucksacks in data:
        rs, comp = set(rucksacks[0]), set(rucksacks[1])
        item = rs.intersection(comp).pop()
        priority += item_to_index(item)
    return priority


def item_to_index(item):
    if item.islower():
        return string.ascii_lowercase.index(item) + 1
    return string.ascii_uppercase.index(item) + 27


def part2(data):
    i = 0
    priority = 0
    while i < len(data):
        elf1, elf2, elf3 = set(data[i]), set(data[i + 1]), set(data[i + 2])
        item = elf1.intersection(elf2, elf3).pop()
        priority += item_to_index(item)
        i += 3
    return priority


def solve(puzzle_input):
    data, data2 = parse(puzzle_input)
    sol1 = part1(data)
    sol2 = part2(data2)
    return sol1, sol2


def run():
    puzzle_input = pathlib.Path("input").read_text().strip()
    solutions = solve(puzzle_input)
    print(solutions)


run()
