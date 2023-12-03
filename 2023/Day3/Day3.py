import math
import pathlib


def parse(puzzle_input):
    values = puzzle_input.split("\n")
    data = []
    for i in range(len(values[0])):
        line = values[i]
        char_list = []
        for j in range(len(line)):
            char_list.append(line[j])
        data.append(char_list)
    return data


def is_adjacent(index, schematic):
    i, j = index
    max_j = len(schematic[0]) - 1
    max_i = len(schematic) - 1
    if i == 0 and j == 0:
        return (schematic[i+1][j] != ".") or \
               (schematic[i+1][j+1] != ".") or \
               (schematic[i][j+1] != "." and not schematic[i][j+1].isdigit())
    elif i == 0 and j == max_j:
        return (schematic[i+1][j] != ".") or \
               (schematic[i+1][j-1] != ".") or \
               (schematic[i][j-1] != "." and not schematic[i][j-1].isdigit())
    elif i == max_i and j == 0:
        return (schematic[i-1][j] != ".") or \
               (schematic[i-1][j+1] != ".") or \
               (schematic[i][j+1] != "." and not schematic[i][j+1].isdigit())
    elif i == max_i and j == max_j:
        return (schematic[i-1][j] != ".") or \
               (schematic[i-1][j-1] != ".") or \
               (schematic[i][j-1] != "." and not schematic[i][j-1].isdigit())
    elif i == 0:
        return (schematic[i+1][j] != ".") or \
               (schematic[i+1][j-1] != ".") or \
               (schematic[i][j-1] != "." and not schematic[i][j-1].isdigit()) or \
               (schematic[i][j+1] != "." and not schematic[i][j+1].isdigit()) or  \
               (schematic[i+1][j+1] != ".")
    elif j == 0:
        return (schematic[i+1][j] != ".") or \
               (schematic[i+1][j+1] != ".") or \
               (schematic[i][j+1] != "." and not schematic[i][j+1].isdigit()) or \
               (schematic[i-1][j+1] != ".") or \
               (schematic[i-1][j] != ".")
    elif i == max_i:
        return (schematic[i-1][j] != ".") or \
               (schematic[i-1][j-1] != ".") or \
               (schematic[i][j-1] != "." and not schematic[i][j-1].isdigit()) or \
               (schematic[i][j+1] != "." and not schematic[i][j+1].isdigit()) or  \
               (schematic[i-1][j+1] != ".")
    elif j == max_j:
        return (schematic[i + 1][j] != ".") or \
               (schematic[i + 1][j - 1] != ".") or \
               (schematic[i][j - 1] != "." and not schematic[i][j - 1].isdigit()) or \
               (schematic[i - 1][j - 1] != ".") or \
               (schematic[i - 1][j] != "." )
    else:
        return (schematic[i+1][j] != ".") or \
               (schematic[i+1][j+1] != ".") or \
               (schematic[i][j+1] != "." and not schematic[i][j+1].isdigit()) or \
               (schematic[i-1][j+1] != ".") or \
               (schematic[i-1][j] != ".") or\
               (schematic[i-1][j-1] != ".") or \
               (schematic[i][j-1] != "." and not schematic[i][j-1].isdigit()) or \
               (schematic[i+1][j-1] != ".")


def part1(schematic):
    number = ""
    result = 0
    adjacent = False
    for i in range(len(schematic)):
        for j in range(len(schematic[0])):
            if schematic[i][j].isdigit():
                number += schematic[i][j]
                if not adjacent:
                    adjacent = is_adjacent((i, j), schematic)
            elif number != "":
                if adjacent:
                    result += int(number)
                number = ""
                adjacent = False
        if number != "":
            if adjacent:
                result += int(number)
            number = ""
            adjacent = False
    return result


def gear_ration(index, schematic):
    i, j = index
    part_numbers = []
    if schematic[i-1][j-1].isdigit():
        part_numbers.append(get_number((i-1, j-1), schematic))
    if schematic[i-1][j].isdigit():
        part_numbers.append(get_number((i-1, j), schematic))
    if schematic[i-1][j+1].isdigit():
        part_numbers.append(get_number((i-1, j+1), schematic))
    if schematic[i][j-1].isdigit():
        part_numbers.append(get_number((i, j-1), schematic))
    if schematic[i+1][j-1].isdigit():
        part_numbers.append(get_number((i+1, j-1), schematic))
    if schematic[i][j+1].isdigit():
        part_numbers.append(get_number((i, j+1), schematic))
    if schematic[i+1][j].isdigit():
        part_numbers.append(get_number((i+1, j), schematic))
    if schematic[i+1][j+1].isdigit():
        part_numbers.append(get_number((i+1, j+1), schematic))
    part_numbers = list(set(part_numbers))
    if len(part_numbers) > 1:
        return math.prod(part_numbers)
    else:
        return 0


def get_number(index, schematic):
    i, j = index
    result = schematic[i][j]
    if schematic[i][j-1].isdigit() and schematic[i][j+1].isdigit():
        return int(schematic[i][j-1] + result + schematic[i][j+1])
    elif schematic[i][j-1].isdigit() and schematic[i][j-2].isdigit():
        return int(schematic[i][j-2] + schematic[i][j-1] + result)
    elif schematic[i][j+1].isdigit() and schematic[i][j+2].isdigit():
        return int(result + schematic[i][j+1] + schematic[i][j+2])
    elif schematic[i][j+1].isdigit():
        return int(result + schematic[i][j+1])
    elif schematic[i][j-1].isdigit():
        return int(schematic[i][j-1] + result)
    else:
        return int(result)


def part2(schematic):
    number = 0
    result = 0
    adjacent = False
    for i in range(len(schematic)):
        for j in range(len(schematic[0])):
            if schematic[i][j] == "*":
                result += gear_ration((i, j), schematic)
    return result


def solve(puzzle_input):
    data = parse(puzzle_input)
    sol1 = part1(data)
    # data = parse(puzzle_input)
    sol2 = part2(data)
    return sol1, sol2


def run():
    puzzle_input = pathlib.Path("input").read_text().strip()
    solutions = solve(puzzle_input)
    print(solutions)


run()
