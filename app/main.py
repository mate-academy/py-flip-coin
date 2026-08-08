import random


def flip_coin() -> dict:
    possible_heads = {
        0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0
    }
    variants = ["head", "tail"]
    for _ in range(10000):
        count = 0
        for _ in range(10):
            variant = random.choice(variants)
            if variant == "head":
                count += 1
        possible_heads[count] += 0.01

    return possible_heads
