import random


def flip_coin():
    results = {i: 0 for i in range(11)}

    for _ in range(10000):
        heads = 0
        for _ in range(10):
            if random.randint(0, 1):
                heads += 1
        results[heads] += 1

    # перевести в відсотки
    for key in results:
        results[key] = round(results[key] / 100, 2)

    return results
