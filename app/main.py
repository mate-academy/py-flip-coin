import random


def flip_coin():
    result = {j: 0 for j in range(11)}

    for _ in range(10000):
        hits = 0

        for _ in range(10):
            choice = random.choice(["eagle", "tails"])
            if choice == "eagle":
                hits += 1

        result[hits] += 1

    return {key: value / 100 for key, value in result.items()}
