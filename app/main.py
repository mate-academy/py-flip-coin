import random


def flip_coin() -> dict[str, int]:
    counts = {heads: 0 for heads in range(11)}
    for _ in range(10000):
        head = 0
        for _ in range(10):
            if random.randint(0, 1) == 1:
                head += 1
        counts[head] += 1
    return {heads: count / 10000 * 100 for heads, count in counts.items()}
