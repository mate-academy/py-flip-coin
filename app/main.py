import random


def flip_coin() -> dict:
    coin_sides = ["heads", "tails"]
    head_comes_up = {i: 0 for i in range(0, 11)}
    total_heads = []
    for _ in range(10000):
        heads_amount = 0
        for _ in range(10):
            if random.choice(coin_sides) == "heads":
                heads_amount += 1
        total_heads.append(heads_amount)

    for key in head_comes_up:
        head_comes_up[key] = round(
            (total_heads.count(key) / len(total_heads) * 100), 2
        )

    return head_comes_up
