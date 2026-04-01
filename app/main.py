import random


def flip_coin() -> dict:
    heads_probability = {i: 0 for i in range(11)}
    for _ in range(10000):
        moves = 0
        for i in range(10):
            if random.choice(["heads", "tail"]) == "heads":
                moves += 1
        heads_probability[moves] += 1
    for key in heads_probability:
        heads_probability[key] = round(
            (heads_probability[key] / 10000) * 100, 2)
    return heads_probability
