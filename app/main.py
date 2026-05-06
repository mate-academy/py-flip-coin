import random


def flip_coin() -> dict:

    coin_flip_results = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0
    }
    heds_tails = ["heads", "tails"]

    for _ in range(10000):
        heads = 0
        for _ in range(10):
            flip = random.choice(heds_tails)
            if flip == "heads":
                heads += 1

        coin_flip_results[heads] = coin_flip_results.get(heads) + 1

    for key in coin_flip_results.keys():
        coin_flip_results[key] = coin_flip_results.get(key) / 10000 * 100

    return coin_flip_results
