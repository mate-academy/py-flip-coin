import random


def flip_coin() -> dict:
    cases = 10000
    sides = ["Heads", "Tails"]
    rounds = {key: 0 for key in range(11)}

    for i in range(cases):
        heads = [random.choice(sides) for _ in range(10)].count("Heads")
        rounds[heads] += 1

    return {key: value * 0.01 for key, value in rounds.items()}
