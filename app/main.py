import random


def flip_coin(number_of_flips: int = 10000) -> dict:
    flips = []
    for i in range(number_of_flips):
        heads = 0
        for _ in range(10):
            result = random.choice(["heads", "tails"])
            if result == "heads":
                heads += 1
        flips.append(heads)
    percentage = {}
    for i in sorted(flips):
        percentage[i] = flips.count(i) / 100
    return percentage
