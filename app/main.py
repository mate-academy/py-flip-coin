import random


def flip_coin():
    cases = 10000

    results = {}
    for i in range(11):
        results[i] = 0

    for _ in range(cases):
        heads_count = 0

        for _ in range(10):
            coin = random.randint(0, 1)
            if coin == 1:
                heads_count += 1

        results[heads_count] += 1

    for key in results:
        results[key] = round((results[key] / cases) * 100, 2)

    return results


print(flip_coin())
