import random


def flip_coin() -> dict:
    seb = [i for i in range(11)]
    seb = {i: 0 for i in seb}
    variants = ["heads", "tails"]
    for _ in range(10000):
        count = 0
        for _ in range(10):
            if random.choice(variants) == "heads":
                count += 1
        seb[count] += 1
    seb = {i: v / 100 for i, v in seb.items()}
    return seb


print(flip_coin())
