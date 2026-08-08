import random


def flip_coin() -> dict:
    trials = 10000
    results = {i: 0 for i in range(11)}

    for _ in range(trials):
        heads = sum(random.choice([0, 1]) for _ in range(10))
        results[heads] += 1

    # Преобразуем в проценты
    for key in results:
        results[key] = round(results[key] / trials * 100, 2)
    return results
