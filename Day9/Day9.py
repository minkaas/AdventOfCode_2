import copy
import pathlib


def parse(puzzle_input):
    values = puzzle_input.split("\n")
    data = []
    for value in values:
        directions = value.split(" ")
        data.append((directions[0], int(directions[1])))
    return data


def are_touching(tail, head):
    return abs(tail[0] - head[0]) <= 1 and abs(tail[1] - head[1]) <= 1


def fix_2knots(tail, head):
    same_row, same_column = not(tail[0]-head[0]), not(tail[1]-head[1])
    pos_row, pos_column = 1 if head[0] - tail[0] > 0 else -1, 1 if head[1] - tail[1] > 0 else -1
    touching = are_touching(tail, head)
    if not same_row and not same_column and not touching:
        tail = (tail[0]+pos_row, tail[1]+pos_column)
    elif not same_row and not touching:
        tail = (tail[0]+pos_row, tail[1])
    elif not same_column and not touching:
        tail = (tail[0], tail[1]+pos_column)
    return tail



def part1(data):
    tail = (0,0)
    head = (0,0)    # (x, y)
    positions = [tail]
    for direction in data:
        richting = direction[0]
        steps = direction[1]
        for step in range(0, steps):
            if richting == "L":
                head = (head[0]-1, head[1])
            elif richting == "U":
                head = (head[0], head[1]+1)
            elif richting == "R":
                head = (head[0]+1, head[1])
            elif richting == "D":
                head = (head[0], head[1]-1)
            tail = fix_2knots(tail, head)
            positions.append(tail)
    return len(set(positions))


def part2(data):
    tails = []
    for i in range(0, 10):
        tails.append((0,0))
    positions = [tails[9]]
    for direction in data:
        richting = direction[0]
        steps = direction[1]
        head = tails[0]
        for step in range(0, steps):
            if richting == "L":
                head = (head[0]-1, head[1])
            elif richting == "U":
                head = (head[0], head[1]+1)
            elif richting == "R":
                head = (head[0]+1, head[1])
            elif richting == "D":
                head = (head[0], head[1]-1)
            tails[0] = head
            for i in range(1, len(tails)):
                tails[i] = fix_2knots(tails[i], tails[i-1])
            positions.append(tails[9])
    return len(set(positions))

def solve(puzzle_input):
    data = parse(puzzle_input)
    sol1 = part1(data)
    sol2 = part2(data)
    return sol1, sol2


def run():
    puzzle_input = pathlib.Path("input").read_text().strip()
    solutions = solve(puzzle_input)
    print(solutions)


run()
