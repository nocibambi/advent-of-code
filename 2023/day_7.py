# %%
from functools import reduce
import re
from itertools import permutations, combinations, chain
import math as m
from pprint import pprint
from typing import Sequence
from collections import Counter
import os
import requests
from pprint import pprint

# %%


def get_input(day: int) -> str:
    return (
        requests.get(
            f"https://adventofcode.com/2023/day/{day}/input",
            cookies={"session": os.environ["AOC_SESSION_COOKIE"]},
        )
        .text.rstrip("\n")
        .split("\n")
    )


# %%
input = get_input(7)
# %%
example = [
    "32T3K 765",
    "T55J5 684",
    "KK677 28",
    "KTJJT 220",
    "QQQJA 483",
]


# %%
def parse_input(input):
    return [line.split(" ") for line in input]


# %%
hand_size = 5

# %%
label_order = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
label_order = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]


# %%
def replace_J_w_most_frequent(hand):
    if hand == "JJJJJ":
        return "AAAAA"
    most_frequent = sorted(
        Counter(hand.replace("J", "")),
        key=lambda x: Counter(hand.replace("J", ""))[x],
    )[::-1][0]

    return hand.replace("J", most_frequent)


def is_five_of_a_kind(hand):
    hand = replace_J_w_most_frequent(hand)
    return max(Counter(hand).values()) == 5


def is_four_of_a_kind(hand):
    hand = replace_J_w_most_frequent(hand)
    return max(Counter(hand).values()) == 4


def is_full_house(hand):
    hand = replace_J_w_most_frequent(hand)
    return set(Counter(hand).values()) == {2, 3}


def is_three_of_a_kind(hand):
    hand = replace_J_w_most_frequent(hand)
    return max(Counter(hand).values()) == 3


def is_two_pair(hand):
    # if can change to two pair, can change to three kind so not needed
    return Counter(Counter(hand).values()) == Counter({2: 2, 1: 1})


def is_one_pair(hand):
    hand = replace_J_w_most_frequent(hand)
    return Counter(Counter(hand).values()) == Counter({2: 1, 1: 3})


def is_high_hand(hand):
    return Counter(Counter(hand).values()) == Counter({1: 5})


# %%
def value_type(hand):
    if is_five_of_a_kind(hand):
        return 7
    if is_four_of_a_kind(hand):
        return 6
    if is_full_house(hand):
        return 5
    if is_three_of_a_kind(hand):
        return 4
    if is_two_pair(hand):
        return 3
    if is_one_pair(hand):
        return 2
    if is_high_hand(hand):
        return 1
    else:
        return 0


def value_cards(hand):
    card_base_value = 0
    for i, card in enumerate(hand):
        for value, label in enumerate(reversed(label_order)):
            if card == label:
                card_base_value += value * 10 ** ((hand_size - i - 1) * 2)
    return card_base_value


def value_hand(hand):
    type_value = value_type(hand) * 10 ** (hand_size * 2)
    cards_value = value_cards(hand)
    return type_value + cards_value


# %%
hands = parse_input(input)
for hand in hands:
    hand.append(value_hand(hand[0]))

sorted_values = sorted([hand[2] for hand in hands])

for hand in hands:
    hand.append(sorted_values.index(hand[2]) + 1)
    hand.append(int(hand[1]) * hand[3])

assert Counter(Counter([hand[2] for hand in hands]).values()) == Counter(
    {1: len(hands)}
)

pprint(hands)
sum([hand[4] for hand in hands])
# %%
