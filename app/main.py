import random


def flip_coin() -> dict:
    final_result = {i: 0 for i in range(11)}
    for _ in range(10000):
        counter = 0
        for _ in range(10):
            flip = random.choice([0, 1])
            if flip == 1:
                counter += 1
        final_result[counter] += 1
    for key, value in final_result.items():
        final_result[key] = (value / 10000) * 100
    return final_result
