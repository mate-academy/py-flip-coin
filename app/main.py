import random


def flip() -> str:
    return random.choice(["Heads", "Tails"])


def count_heads() -> int:
    heads_total = 0
    for number in range(10):
        if flip() == "Heads":
            heads_total += 1
    return heads_total


def flip_coin() -> dict:
    count_flips = {key: 0 for key in range(11)}
    for number in range(10000):
        count_flips[count_heads()] += 1

    percentage_count_flips = {}
    for number in range(11):
        percentage_count_flips[number] = (
            round((count_flips[number] / 100), 2))
    return percentage_count_flips
