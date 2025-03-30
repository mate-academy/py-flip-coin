from random import randint


def flip_coin() -> dict:
    result = {i: 0 for i in range(11)}
    for _ in range(10000):
        flipping_streak = [randint(0, 1) for _ in range(10)]
        key = flipping_streak.count(0)
        result[key] += 1
    final_result = {key: round(value / 10000 * 100, 2)
                    for key, value in result.items()}
    return final_result
