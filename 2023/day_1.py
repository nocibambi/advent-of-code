# %%
with open("input_1.txt", "r") as f:
    inputs = f.read().splitlines()
# %%
inputs
# %%
values = []
for input in inputs:
    digits = [i for i in input if i.isdigit()]
    values.append(int(digits[0] + digits[-1]))

# %%
sum(values)
# %%
digits_map = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}
# %%
values = []
for input in inputs:
    input_digits = []
    for i, c in enumerate(input):
        if c.isdigit():
            input_digits.append(c)

        for number in digits_map.keys():
            if input[i:].startswith(number):
                input_digits.append(digits_map[number])

    values.append(int(input_digits[0] + input_digits[-1]))

sum(values)
# %%
