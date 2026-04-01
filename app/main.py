from random import randint


def flip_coin() -> dict:
    flip_results = []
    results_of_flipping_heads = {}
    for _ in range(10000):
        flip_coin_10_times = [randint(0, 1) for _ in range(10)]
        flip_results.append(flip_coin_10_times.count(1))
    for i in range(11):
        results_of_flipping_heads[i] = round(flip_results.count(i) / 100, 2)
    return results_of_flipping_heads
