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


def hey_i_know_these_2_knots_should_be_closer_together_fix_that(tail, head):
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


def part2(data, knots):
    tails = []
    for i in range(0, knots+1):
        tails.append((0,0))
    positions = [tails[knots]]
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
                tails[i] = hey_i_know_these_2_knots_should_be_closer_together_fix_that(tails[i], tails[i - 1])
            positions.append(tails[knots])
    return len(set(positions))


def solve(puzzle_input):
    data = parse(puzzle_input)
    sol1 = part2(data, 1)
    sol2 = part2(data, 9)
    return sol1, sol2


def run():
    puzzle_input = pathlib.Path("input").read_text().strip()
    solutions = solve(puzzle_input)
    print(solutions)


run()
