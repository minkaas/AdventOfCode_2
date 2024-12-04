import pathlib
from time import time
import re

def parse(puzzle_input):
    values = puzzle_input.split("\n")
    data = []
    for value in values:
        data.append(value)
    return data


def search_horizontal(line, x):
    result = set()
    counter = 0
    for i in range(0, len(line) - 3):
        if line[i] + line[i+1] + line[i+2] + line[i+3] == "XMAS" or line[i] + line[i+1] + line[i+2] + line[i+3] == "SAMX":
            result.add((x, i))
            result.add((x, i+1))
            result.add((x, i+2))
            result.add((x, i+3))
            counter += 1
    return result, counter


def search_vertical(l1, l2, l3, l4, x):
    result = set()
    counter = 0
    for y in range(0, len(l1)):
        if l1[y] + l2[y] + l3[y] + l4[y] == "XMAS" or l1[y] + l2[y] + l3[y] + l4[y] == "SAMX":
            result.add((x, y))
            result.add((x+1, y))
            result.add((x+2, y))
            result.add((x+3, y))
            counter += 1
    return result, counter


def search_diagonal(l1, l2, l3, l4, x):
    result = set()
    counter = 0
    # to the right
    for y in range(0, len(l1) - 3):
        if l1[y] + l2[y+1] + l3[y+2] + l4[y+3] == "XMAS" or l1[y] + l2[y+1] + l3[y+2] + l4[y+3] == "SAMX":
            result.add((x,y))
            result.add((x+1, y+1))
            result.add((x+2, y+2))
            result.add((x+3, y+3))
            counter += 1
    # to the left
    for y in range(3, len(l1)):
        if l1[y] + l2[y-1] + l3[y-2] + l4[y-3] == "XMAS" or l1[y] + l2[y-1] + l3[y-2] + l4[y-3] == "SAMX":
            result.add((x, y))
            result.add((x+1, y-1))
            result.add((x+2, y-2))
            result.add((x+3, y-3))
            counter += 1
    return result, counter


def part1(data):
    horizontal, counter = search_horizontal(data[0], 0)
    horizontal, counter = horizontal.union(search_horizontal(data[1], 1)[0]), counter + search_horizontal(data[1], 1)[1]
    horizontal, counter = horizontal.union(search_horizontal(data[2], 2)[0]), counter + search_horizontal(data[2], 2)[1]
    vertical = set()
    diagonal = set()
    for i in range(3, len(data)):
        hori, value = search_horizontal(data[i], i)
        horizontal, counter = horizontal.union(hori), counter + value
        vert, value = search_vertical(data[i-3], data[i-2], data[i-1], data[i], i-3)
        vertical, counter = vertical.union(vert), counter + value
        diag, value = search_diagonal(data[i-3], data[i-2], data[i-1], data[i], i-3)
        diagonal, counter = diagonal.union(diag), counter + value
    result = horizontal.union(vertical).union(diagonal)
    return counter


def print_matrix(result_set, data):
    for i in range(0, len(data)):
        result = ""
        for j in range(0, len(data[i])):
            if (i, j) in result_set:
                result += data[i][j]
            else:
                result += "."
        print(result)


def search_cross(l1, l2, l3, x):
    result = set()
    counter = 0
    for i in range(0, len(l1)-2):
        if l2[i+1] == "A" and ((l1[i] == l1[i+2] and l3[i] == l3[i+2]) or (l1[i] == l3[i] and l1[i+2] == l3[i+2])) and l1[i] != 'X' and l1[i+2] != 'X' and l3[i] != 'X':
            if l1[i] + l2[i+1] + l3[i+2] == "MAS" or l1[i] + l2[i+1] + l3[i+2] == "SAM":
                result.add((x, i))
                result.add((x, i+2))
                result.add((x+1, i+1))
                result.add((x+2, i))
                result.add((x+2, i+2))
                counter += 1
    return result, counter


def part2(data):
    result_set, counter = set(), 0
    for i in range(0, len(data)-2):
        crosses, value = search_cross(data[i], data[i+1], data[i+2], i)
        result_set = result_set.union(crosses)
        counter += value
    print_matrix(result_set, data)
    return counter


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
