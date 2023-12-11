import pathlib
from time import time


def parse(puzzle_input):
    values = puzzle_input.split("\n")
    data = []
    for value in values:
        value = value.split(":")[1]
        left, right = value.split("|")[0].split(" "), value.split("|")[1].split(" ")
        data.append((left, right))
    return data


def amount_winning(card):
    winning = []
    left, right = card
    left = [i for i in left if i != ""]
    right = [i for i in right if i != ""]
    for value in left:
        winning.append(int(value))
    for value in right:
        winning.append(int(value))
    no_dupes = len(winning)
    winning = list(set(winning))
    worthy_cards = no_dupes - len(winning)
    return worthy_cards


def part1(cards):
    result = 0
    for card in cards:
        worthy_cards = amount_winning(card)
        if worthy_cards:
            result += pow(2, worthy_cards-1)
    return result


def part2(cards):
    card_copies = [0] * len(cards)
    for i in range(len(cards)):
        card_copies[i] += 1
        worthy_cards = amount_winning(cards[i])
        for j in range(i+1, i+1+worthy_cards):
            card_copies[j] += card_copies[i]
    return sum(card_copies)


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
