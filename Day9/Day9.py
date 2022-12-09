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


def fix_2knots(tail, head, prev):
    same_column = tail[0]-head[0] == 0   #(0,0), (2,2)
    same_row = tail[1]-head[1] == 0
    pos_row = 1 if head[1] - tail[1] > 0 else -1
    pos_column = 1 if head[0] - tail[0] > 0 else -1
    touching = are_touching(tail, head)
    if not same_row and not same_column and not touching:
        tail = (tail[0]+pos_column, tail[1]+pos_row)
    elif not same_row and not touching:
        tail = (tail[0], tail[1]+pos_row)
    elif not same_column and not touching:
        tail = (tail[0]+pos_column, tail[1])
    return tail



def part1(data):
    tail = (0,0)
    head = (0,0)    # (x, y)
    prevhead = head
    positions = [tail]
    for direction in data:
        dir = direction[0]
        steps = direction[1]
        for step in range(0, steps):
            prevhead = head
            if dir == "L":      #(x-1, y)
                head = (head[0]-1, head[1])
            elif dir == "U":    #(x, y+1
                head = (head[0], head[1]+1)
            elif dir == "R":
                head = (head[0]+1, head[1])
            elif dir == "D":
                head = (head[0], head[1]-1)
            if not are_touching(tail, head):
                tail = prevhead
                positions.append(tail)
    return len(set(positions))


def part2(data):
    tails = []
    for i in range(0, 9):
        tails.append((0,0))
    head = (0, 0)    # (x, y)
    prevhead = head
    prevtails = copy.deepcopy(tails)
    positions = [tails[8]]
    for direction in data:
        dir = direction[0]
        steps = direction[1]
        for step in range(0, steps):
            prevhead = head
            prevtails = copy.deepcopy(tails)
            if dir == "L":      #(x-1, y)
                head = (head[0]-1, head[1])
            elif dir == "U":    #(x, y+1
                head = (head[0], head[1]+1)
            elif dir == "R":
                head = (head[0]+1, head[1])
            elif dir == "D":
                head = (head[0], head[1]-1)
            for i in range(0, len(tails)):
                if i == 0:
                    tails[0] = fix_2knots(tails[0], head, prevhead)
                else:
                    tails[i] = fix_2knots(tails[i], tails[i-1], prevtails[i-1])
            positions.append(tails[8])
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
