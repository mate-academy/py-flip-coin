import random


def flip_coin() -> dict:
    total_heads_count = 0
    result = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0,
              6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
    options = ["heads", "tails"]
    for _ in range(10000):
        this_try_heads_count = 0
        for _ in range(10):
            choice = random.choice(options)
            if choice == "heads":
                this_try_heads_count += 1
                total_heads_count += 1
        result[this_try_heads_count] += 1
    for key, value in result.items():
        result[key] = value / 10000 * 100

    return result
