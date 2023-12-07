# %%
from functools import reduce
import re
from itertools import permutations, combinations
import math as m
from pprint import pprint
from typing import Sequence

from collections import Counter


# %%
with open("input_4.txt", "r") as f:
    inputs = f.read().splitlines()

inputs


# %%
def clean_seq(string: Sequence[str], sep=" "):
    return [s.strip() for s in string.split(" ") if s]


# %%

# line = inputs[0]
# line
# %%
points = list()
for line in inputs:
    winning = clean_seq(line.split(": ")[1].split(" | ")[0])
    available = clean_seq(line.split(": ")[1].split(" | ")[1])
    matches = len(set(winning).intersection(set(available)))
    points.append(2 ** (matches - 1) // 1)

points
# %%
sum(points)
# %%


# %%
multipliers = Counter()
# %%
line = inputs[1]

game_number = int(line.split(": ")[0].replace("Card ", "").strip())
winning = clean_seq(line.split(": ")[1].split(" | ")[0])
available = clean_seq(line.split(": ")[1].split(" | ")[1])
matches = set(winning).intersection(set(available))
num_matches = len(matches)
additions = Counter(
    list(range(game_number + 1, game_number + num_matches + 1))
)
multipliers += Counter(
    {
        card: additions[card] * multipliers.get(game_number, 1)
        for card in additions
    }
)
print(game_number, multipliers)
# %%

# %%
multipliers = Counter(range(len(inputs)))
for line in inputs:
    game_number = int(line.split(": ")[0].replace("Card ", "").strip())
    winning = clean_seq(line.split(": ")[1].split(" | ")[0])
    available = clean_seq(line.split(": ")[1].split(" | ")[1])
    matches = set(winning).intersection(set(available))
    num_matches = len(matches)
    additions = Counter(
        list(range(game_number + 1, game_number + num_matches + 1))
    )
    multipliers += Counter(
        {card: multipliers.get(game_number) for card in additions}
    )
    print(game_number, num_matches, list(additions.keys()), multipliers)

multipliers

# %%
sum(multipliers.values())

# %%
11699039

# %%

# %%
