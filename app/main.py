import random


def flip_coin(trials: int = 10000) -> dict:
    results = {i: 0 for i in range(11)}  # від 0 до 10 решок

    for _ in range(trials):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        results[heads_count] += 1

    for round_result in results:
        results[round_result] = round(results[round_result] / trials * 100, 2)

    return results


print(flip_coin())
