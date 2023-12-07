# %%
from functools import reduce
import re
from itertools import permutations, combinations
import math as m
from pprint import pprint
from typing import Sequence
from collections import Counter

# %%
with open("input_6.txt", "r") as f:
    inputs = f.read().rstrip("\n")
inputs.split("\n")
# %%
times = list(
    map(
        int,
        [
            v
            for v in re.sub(
                r"\s+", ",", inputs.split("\n")[0].split(r":")[1].lstrip()
            ).split(",")
        ],
    )
)
records = list(
    map(
        int,
        [
            v
            for v in re.sub(
                r"\s+", ",", inputs.split("\n")[1].split(r":")[1].lstrip()
            ).split(",")
        ],
    )
)

times, records
# %%
# i = 0
# time, record = times[i], records[i]
# time, record = 7, 9

# times = [7, 15, 30]
# records = [9, 40, 200]

successes = list()
for i in range(len(times)):
    print(i), print()
    num_success = 0
    for hold in list(range(times[i] + 1)):
        distance = hold * (times[i] - hold)
        if distance > records[i]:
            num_success += 1
        print(hold, distance)

    successes.append(num_success)

successes
# %%
reduce(lambda x, y: x * y, successes)
# %%
time = int(re.sub(r"\s+", "", inputs.split("\n")[0].split(r":")[1].lstrip()))
record = int(re.sub(r"\s+", "", inputs.split("\n")[1].split(r":")[1].lstrip()))

time, record
# %%
# time = 71530
# record = 940200
# %%
num_success = 0
for hold in list(range(time + 1)):
    speed = time - hold
    distance = hold * speed
    if distance > record:
        num_success += 1
        print(hold, speed, distance, record, num_success)
        break

num_success
# %%
speed - hold + 1
# %%
record 