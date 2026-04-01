import random


def flip_coin() -> dict:

    choices = ["head", "tail"]
    counter = {i: 0 for i in range(11)}

    for _ in range(10000):
        heads_counter = 0

        for _ in range(10):
            result = random.choice(choices)
            heads_counter += (result == "head")

        counter[heads_counter] += 1

    return {key: value / 100 for key, value in counter.items()}
