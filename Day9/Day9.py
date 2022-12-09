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


def are_touching_10(tails, head):
    tail = tails[0]
    if abs(tail[0] - head[0]) <= 1 and abs(tail[1] - head[1]) <= 1:
        for i in range(1, len(tails)):
            if not abs(tails[i][0] - tails[i-1][0]) <= 1 or not abs(tails[i][1] - tails[i-1][1]) <= 1:
                return False, i
    else:
        return False, 0
    return True, 0



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
    positions = [tails[8]]
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
            are_touching, which_head = are_touching_10(tails, head)
            if not are_touching:
                prevtail = prevhead
                while not are_touching:
                    prev = tails[which_head]
                    tails[which_head] = prevtail
                    are_touching, which_head = are_touching_10(tails, head)
                    prevtail = prev
                positions.append(tails[8])
    return len(set(positions))

def solve(puzzle_input):
    data = parse(puzzle_input)
    sol1 = part1(data)
    sol2 = part2(data)
    return sol1, sol2


def run():
    puzzle_input = pathlib.Path("test").read_text().strip()
    solutions = solve(puzzle_input)
    print(solutions)


run()
