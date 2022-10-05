import random


def flip_coin() -> dict:
    sides = ("heads", "tails")
    data = {i: 0 for i in range(11)}
    for num in range(10000):
        counter = 0
        for n in range(10):
            if random.choice(sides) == "heads":
                counter += 1
        data[counter] += 1
    result = {key: value / 100 for key, value in data.items()}
    return result
