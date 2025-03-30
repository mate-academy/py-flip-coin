from random import random


def flip_coin() -> dict:
    num_cases = 10000
    num_flips = 10
    result = {}

    for num in range(num_cases):
        num_heads = 0
        for _ in range(num_flips):
            if random() < 0.5:
                num_heads += 1
        result[num_heads] = result.get(num_heads, 0) + 1
    chances = {}
    for num_heads, count in result.items():
        chance = count / num_cases * 100
        chances[num_heads] = round(chance, 2)
    return chances
