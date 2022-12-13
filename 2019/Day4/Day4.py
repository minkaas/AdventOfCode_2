import pathlib


def parse():
    return [272091, 815432]


def part1(data):
    count = 0
    for i in range(data[0], data[1]+1):
        j = [int(k) for k in str(i)]
        counting = True
        adjacent = False
        for k in range(1, 6):
            if not j[k-1] <= j[k]:
                counting = False
            if j[k-1] == j[k]:
                adjacent = True
        if counting and adjacent:
            count += 1
    return count


def part2(data):
    return 0


def solve():
    data = parse()
    sol1 = part1(data)
    sol2 = part2(data)
    return sol1, sol2


def run():
    solutions = solve()
    print(solutions)


run()
