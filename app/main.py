import random


def flip_coin() -> dict:
    result = {counter: 0 for counter in range(0, 11)}

    for _ in range(12_000):
        head_counter = 0

        for _ in range(10):
            is_head = random.randint(0, 1)
            if is_head:
                head_counter += 1
        result[head_counter] += 1

    return {key: value / 12_000 * 100 for key, value in result.items()}
