import random


def flip_coin() -> dict:

    flip_dict = {}
    number_of_cases = 10000
    number_of_flips = 10

    for _ in range(number_of_cases):
        count = 0
        for _ in range(number_of_flips):
            if random.choice(["heads", "tails"]) == "heads":
                count += 1
        if count in flip_dict:
            flip_dict[count] += 1
        else:
            flip_dict[count] = 1

    for key, value in flip_dict.items():
        flip_dict[key] = round(value / 100, 2)
    return flip_dict
