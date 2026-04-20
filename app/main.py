import random


def single_flip() -> int:
    heads_count = 0
    for _ in range(10):
        if random.choice([0, 1]) == 1:
            heads_count += 1
    return heads_count


def flip_coin(trials: int = 10000) -> dict[int, float]:
    results = {i: 0 for i in range(11)}
    for _ in range(trials):
        heads_count = single_flip()
        results[heads_count] += 1
    percentages = {k: round((v / trials) * 100, 2) for k, v in results.items()}
    return percentages


result = flip_coin(100000)
