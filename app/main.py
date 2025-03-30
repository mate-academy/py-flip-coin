import random


def flip_coin() -> dict:
    lst_flip = [0] * 11
    for _ in range(10000):
        count_heads = 0
        for _ in range(10):
            coin_side = random.choice(["heads", "tails"])
            count_heads += (1 if coin_side == "heads" else 0)
        lst_flip[count_heads] += 1

    return {
        i: round((count / sum(lst_flip)) * 100, 2)
        for i, count in enumerate(lst_flip)
    }
