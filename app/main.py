import random


def flip_coin() -> dict:
    result = {tally: 0 for tally in range(0, 11)}

    for _ in range(12_000):
        head_tally = 0

        for _ in range(10):
            is_head = random.randint(0, 1)
            if is_head:
                head_tally += 1
        result[head_tally] += 1

    return {key: value / 12_000 * 100 for key, value in result.items()}
