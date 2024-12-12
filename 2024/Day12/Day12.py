import pathlib
from time import time


def parse(puzzle_input):
    values = puzzle_input.split("\n")
    data = []
    padding = [-1] * (len(values[0]) + 2)
    data.append(padding)
    for value in values:
        temp = [-1] + [ord(x) for x in value] + [-1]
        data.append(temp)
    data.append(padding)
    return data


def get_perimeter(area_coords, data):
    look_around = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    perimeter = 0
    for coord in area_coords:
        for look in look_around:
            new = tuple(map(sum, zip(coord, look)))
            if data[new[0]][new[1]] != data[coord[0]][coord[1]]:
                perimeter += 1
    return perimeter


def bread_first_search(data, start):
    look_around = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = [start]
    queue = [start]
    while queue:
        current = queue.pop()
        for look in look_around:
            new = tuple(map(sum, zip(current, look)))
            if data[new[0]][new[1]] == data[current[0]][current[1]] and new not in visited:
                visited.append(new)
                queue.append(new)
    return visited


def part1(data):
    result = 0
    area_coords = {}
    for i in range(1, len(data)-1):
        for j in range(1, len(data)-1):
            if data[i][j] not in area_coords:
                coords = bread_first_search(data, (i, j))
                area_coords[data[i][j]] = coords
                result += len(coords) * get_perimeter(coords, data)
            elif (i, j) not in area_coords[data[i][j]]:
                coords = bread_first_search(data, (i, j))
                area_coords[data[i][j]] = area_coords[data[i][j]] + coords
                result += len(coords) * get_perimeter(coords, data)
    return result


def get_num_sides(area_coords, data):
    corners = [[(0, 1), (1, 0), (1, 1)], [(0, -1), (-1, 0), (-1, -1)], [(0, 1), (-1, 0), (-1, 1)], [(0, -1), (1, 0), (1, -1)]]
    sides = 0
    if len(area_coords) == 1:
        return 4
    for coord in area_coords:
        for corn in corners:
            temp = data[coord[0]][coord[1]]
            one = tuple(map(sum, zip(coord, corn[0])))
            two = tuple(map(sum, zip(coord, corn[1])))
            diag = tuple(map(sum, zip(coord, corn[2])))
            if diag not in area_coords and (data[one[0]][one[1]] == data[two[0]][two[1]] or (data[one[0]][one[1]] != temp and data[two[0]][two[1]] != temp)):
                sides += 1
            elif diag in area_coords and data[one[0]][one[1]] != temp and data[two[0]][two[1]] != temp:
                sides += 1
    return sides


def part2(data):
    result = 0
    area_coords = {}
    for i in range(1, len(data)-1):
        for j in range(1, len(data)-1):
            if data[i][j] not in area_coords:
                coords = bread_first_search(data, (i, j))
                area_coords[data[i][j]] = coords
                print(chr(data[i][j]), get_num_sides(coords, data))
                result += len(coords) * get_num_sides(coords, data)
            elif (i, j) not in area_coords[data[i][j]]:
                coords = bread_first_search(data, (i, j))
                area_coords[data[i][j]] = area_coords[data[i][j]] + coords
                print(chr(data[i][j]), get_num_sides(coords, data))
                result += len(coords) * get_num_sides(coords, data)
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
