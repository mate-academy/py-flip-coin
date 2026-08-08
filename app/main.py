import random


def flip_coin() -> dict:
    temp_result = {i: 0 for i in range(11)}
    variants = ["heads", "tails"]
    for _ in range(10000):
        count = 0
        for _ in range(10):
            if random.choice(variants) == "heads":
                count += 1
        temp_result[count] += 1
    result = {k: v / 100 for k, v in temp_result.items()}
    return result


print(flip_coin())
