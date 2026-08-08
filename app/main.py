import random as r


def flip_coin() -> dict[int, float]:
    flips = [
        sum(r.randint(0, 1)
            for _ in range(10))
        for _ in range(10000)
    ]
    result: dict = {
        i: round(((flips.count(i) / 10000) * 100), 2)
        for i in range(11)
    }

    return result
