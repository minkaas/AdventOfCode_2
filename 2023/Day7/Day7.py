import pathlib
import re
from time import time


def parse(puzzle_input):
    values = puzzle_input.split("\n")
    data = []
    for value in values:
        hand, card = value.split(" ")
        data.append((hand, int(card)))
    return data


# 1 high, 2 - one pair, 3 two pair etc
def get_rank(card):
    hand = card[0]
    first = hand[0]
    second = hand[1]
    third = hand[2]
    fourth = hand[3]
    fifth = hand[4]
    if first == second == third == fourth == fifth:
        return 7
    if hand.count(first) == 4 or hand.count(second) == 4:
        return 6
    if len(list(set(list(hand)))) == 2:
        return 5
    if hand.count(first) == 3 or hand.count(second) == 3 or hand.count(third) == 3:
        return 4
    if len(list(set(list(hand)))) == 3 and (hand.count(first) != 4 and hand.count(second) != 4):
        return 3
    if len(list(set(list(hand)))) == 4:
        return 2
    if len(list(set(list(hand)))) == 5:
        return 1


def get_joker_rank(card):
    hand, value = card
    hand = [i for i in hand if i != 'J']
    if len(hand) == 5 or len(hand) == 0:  # if no jokers its same as always
        return get_rank(card)
    else:
        unique = len(list(set(list(hand))))  # unique numbers
        if unique == 1:  # If the hand was like AAJJJ, unique without JJJ will be A
            return 7
        if unique == 2 and len(hand) == 4 and get_rank(card) == 3:  # previously 2 pair with one J makes it full house
            return 5
        if unique == 2:  # otherwise it can be JJJAQ, JJAAQ, JAAAQ which are all 4 of a kind
            return 6
        if unique == 3:  # JAA23 JJA23, always 3 of a kind
            return 4
        if unique == 4:  # J2345 will always ideally be 1 pair
            return 2


def add_ranked_cards(card, result, joker):
    rank = 0
    if joker:
        rank = get_joker_rank(card)
    else:
        rank = get_rank(card)
    hand, value = card
    result.append((hand, value, rank))
    return result


def compare_card_values(value1, value2, hand1, hand2, joker):
    if joker:
        re.sub(hand1, 'J', '1')
        re.sub(hand2, 'J', '1')
        if value1 == 'J':
            value1 = '1'
        if value2 == 'J':
            value2 = '1'
    if value1 == value2:
        return compare_card_values(hand1[1:][0], hand2[1:][0], hand1[1:], hand2[1:], joker)
    if value1.isdigit() and value2.isdigit():
        return int(value1) > int(value2)
    if value1.isdigit():
        return False
    if value2.isdigit():
        return True
    cards = ['T', 'J', 'Q', 'K', 'A']
    return cards.index(value1) > cards.index(value2)


def compare_cards(card1, card2, joker):
    hand, value, rank = card1
    hand1, value1, rank1 = card2
    if rank > rank1:
        return True
    if rank1 > rank:
        return False
    if rank1 == rank:
        return compare_card_values(hand[0], hand1[0], hand, hand1, joker)


def insertion_sort(unsorted_list, joker):
    i = 1
    while i < len(unsorted_list):
        j = i
        one = unsorted_list[j - 1]
        two = unsorted_list[j]
        while j > 0 and compare_cards(unsorted_list[j - 1], unsorted_list[j], joker):
            unsorted_list[j - 1], unsorted_list[j] = unsorted_list[j], unsorted_list[j - 1]
            j -= 1
        i += 1
    return unsorted_list


def part1(data):
    result = []
    final_result = 0
    for (hand, card) in data:
        result = add_ranked_cards((hand, card), result, False)
    result = insertion_sort(result, False)
    for i in range(0, len(result)):
        final_result += result[i][1] * (i + 1)
    return final_result


def part2(data):
    result = []
    final_result = 0
    for (hand, card) in data:
        result = add_ranked_cards((hand, card), result, True)
    result = insertion_sort(result, True)
    print(result)
    for i in range(0, len(result)):
        final_result += result[i][1] * (i + 1)
    return final_result


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
