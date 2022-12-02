import pathlib

def parse(puzzle_input):
    values = puzzle_input.split("\n")
    data = []
    for value in values:
        string1, string2 = value.split(" ")
        data.append([string1, string2])
    return data


def part1(data):
    result = 0
    for strings in data:
        mymove = strings[1]
        theirmove = strings[0]
        if theirmove == "A":      # Rock
            if mymove == "X":     # Rock
                result += 1 + 3
            elif mymove == "Y":   # Paper
                result += 2 + 6
            elif mymove == "Z":   # Scissors
                result += 3 + 0
        elif theirmove == "B":    # Paper
            if mymove == "X":     # Rock
                result += 1 + 0
            elif mymove == "Y":   # Paper
                result += 2 + 3
            elif mymove == "Z":   # Scissors
                result += 3 + 6
        elif theirmove == "C":    # Scissors
            if mymove == "X":     # Rock
                result += 1 + 6
            elif mymove == "Y":   # Paper
                result += 2 + 0
            elif mymove == "Z":   # Scissors
                result += 3 + 3
    return result


def part2(data):
    result = 0
    for strings in data:
        mymove = strings[1]
        theirmove = strings[0]
        if theirmove == "A":      # Rock
            if mymove == "X":     # Lose
                result += 0 + 3
            elif mymove == "Y":   # Draw
                result += 3 + 1
            elif mymove == "Z":   # Win
                result += 6 + 2
        elif theirmove == "B":    # Paper
            if mymove == "X":     # Lose
                result += 0 + 1
            elif mymove == "Y":   # Draw
                result += 3 + 2
            elif mymove == "Z":   # Win
                result += 6 + 3
        elif theirmove == "C":    # Scissors
            if mymove == "X":     # Lose
                result += 0 + 2
            elif mymove == "Y":   # Draw
                result += 3 + 3
            elif mymove == "Z":   # Win
                result += 6 + 1
    return result

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