import random


def flip_coin() -> dict:
    scrim = ["head", "back"]
    result = {num: 0 for num in range(11)}

    for _ in range(10000):
        head_count = sum(
            1 for _ in range(10) if random.choice(scrim) == "head"
        )
        result[head_count] += 1

    for key in result.keys():
        result[key] = round(result[key] / 10000 * 100, 2)

    return result
