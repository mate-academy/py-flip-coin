import random


def flip_coin() -> dict:
    results = {
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
    coin = ["head", "tail"]
    total_heads = []
    for _ in range(10000):
        head_number = 0
        for _ in range(10):
            flip = random.choice(coin)
            if flip == "head":
                head_number += 1
        total_heads.append(head_number)

    for key in results:
        results[key] = round(
            (total_heads.count(key) / len(total_heads) * 100), 2
        )
    return results
