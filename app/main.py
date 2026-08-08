import random


def flip_coin() -> dict[int, float]:
    results = {i: 0 for i in range(11)}

    for _ in range(10000):
        heads = 0

        for _ in range(10):
            if random.random() < 0.5:
                heads += 1

        results[heads] += 1

    for key in results:
        results[key] = round((results[key] / 10000) * 100, 2)

    return results


print(flip_coin())
