from random import randint


def flip_coin() -> dict:
    head = {}
    attempts = 10000
    for _ in range(attempts):
        heads = [randint(0, 1) for _ in range(10)].count(1)
        head[heads] = head.get(heads, 0) + 1

    for key, value in head.items():
        head[key] = round((value / (attempts / 100)), 2)
    return dict(sorted(head.items()))
