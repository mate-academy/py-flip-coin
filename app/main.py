import random


def flip_10_times() -> int:
    return sum([random.randint(0, 1) for _ in range(10)])


def flip_coin() -> dict[int, float | int]:
    heads_count = {i: 0 for i in range(11)}
    simulations_count = 10_000

    for _ in range(0, simulations_count):
        heads = flip_10_times()
        heads_count[heads] += 1

    result = {key: (count / simulations_count) * 100 for key, count in
              heads_count.items()}

    return result
