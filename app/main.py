import random


def flip_coin() -> dict:
    coin = ["heads", "tails"]
    coin_flip = {}
    for _ in range(10000):
        all_heads = 0
        for flip in range(10):
            if random.choice(coin) == "heads":
                all_heads += 1
        if all_heads in coin_flip:
            coin_flip[all_heads] += 1
        else:
            coin_flip[all_heads] = 1
    for key, value in coin_flip.items():
        coin_flip[key] = (value / 10000) * 100
    return coin_flip
