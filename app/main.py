import random


def flip_coin() -> dict[int, float]:
    heads_count = {}

    for _ in range(10_000):
        count = sum(
            1 for _ in range(10)
            if round(random.random()) == 1
        )

        if heads_count.get(count) is None:
            heads_count[count] = 1
        else:
            heads_count[count] += 1

    return {
        heads: (count / 10000) * 100 for heads, count in heads_count.items()
    }
