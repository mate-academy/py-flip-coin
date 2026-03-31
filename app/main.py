import random


def flip_coin() -> None:
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
    for _ in range(10000):
        heads_count = 0

        for _ in range(10):
            random_head = random.randint(0, 1)
            if random_head == 0:
                heads_count += 1

        results[heads_count] += 1

    for key in results:
        results[key] = results[key] / 10000 * 100
    return results
