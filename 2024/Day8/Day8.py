import pathlib
from time import time


def parse(puzzle_input):
    values = puzzle_input.split("\n")
    data = []
    nodes = {}
    for i in range(0, len(values)):
        temp = []
        for j in range(0, len(values[i])):
            temp.append(values[i][j])
            if values[i][j] != '.':
                if values[i][j] in nodes:
                    nodes[values[i][j]].append((i, j))
                else:
                    nodes[values[i][j]] = [(i, j)]
        data.append(temp)
    return data, nodes


def print_matrix(data, coords):
    if len(coords) > 0:
        for i in range(0, len(data)):
            to_print = ""
            for j in range(0, len(data[i])):
                if (i, j) in coords:
                    to_print += '#'
                else:
                    to_print += data[i][j]
            print(to_print)
    else:
        for row in data:
            to_print = ""
            for character in row:
                to_print += character
            print(to_print)


def within_bounds(i, j, data):
    return 0 <= i < len(data) and 0 <= j < len(data[i])


def distance(coord_1, coord_2):
    return coord_1[0] - coord_2[0], coord_1[1] - coord_2[1]


def covered(nodes, coord):
    for node in nodes:
        if coord in nodes[node]:
            return node, coord[0], coord[1]
    else:
        return False


def part1(data, nodes):
    result = []
    antinodes = []
    for node in nodes:
        all_nodes = nodes[node]
        for k in range(0, len(all_nodes)):
            for l in range(k+1, len(all_nodes)):
                coord_1, coord_2 = all_nodes[k], all_nodes[l]
                dist_1, dist_2 = distance(coord_1, coord_2), distance(coord_2, coord_1)
                anti_1, anti_2 = (coord_1[0] + dist_1[0], coord_1[1] + dist_1[1]), (coord_2[0] + dist_2[0], coord_2[1] + dist_2[1])
                if within_bounds(anti_1[0], anti_1[1], data):
                    antinodes.append(anti_1)
                if within_bounds(anti_2[0], anti_2[1], data):
                    antinodes.append(anti_2)
    result = list(set(antinodes))
    return len(result)


def part2(data, nodes):
    result = []
    antinodes = []
    for node in nodes:
        all_nodes = nodes[node]
        for k in range(0, len(all_nodes)):
            for l in range(k+1, len(all_nodes)):
                coord_1, coord_2 = all_nodes[k], all_nodes[l]
                antinodes.append(coord_1)
                antinodes.append(coord_2)
                dist_1, dist_2 = distance(coord_1, coord_2), distance(coord_2, coord_1)
                anti_1, anti_2 = (coord_1[0] + dist_1[0], coord_1[1] + dist_1[1]), (coord_2[0] + dist_2[0], coord_2[1] + dist_2[1])
                while within_bounds(anti_1[0], anti_1[1], data):
                    antinodes.append(anti_1)
                    anti_1 = (anti_1[0] + dist_1[0], anti_1[1] + dist_1[1])
                while within_bounds(anti_2[0], anti_2[1], data):
                    antinodes.append(anti_2)
                    anti_2 = (anti_2[0] + dist_2[0], anti_2[1] + dist_2[1])
    result = list(set(antinodes))
    print_matrix(data, antinodes)
    return len(result)


def solve(puzzle_input):
    data, nodes = parse(puzzle_input)
    sol1 = part1(data, nodes)
    sol2 = part2(data, nodes)
    return sol1, sol2


def run():
    start_time = time()
    puzzle_input = pathlib.Path("input").read_text().strip()
    solutions = solve(puzzle_input)
    print(solutions)
    print("This took ", time() - start_time)

run()
