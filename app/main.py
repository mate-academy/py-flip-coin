import random

def flip_coin() -> dict[int, float]:
    counts = {key: 0 for key in range(11)}

    for i in range(10000):
        how_many = 0
        for _ in range(10):
            coin = random.randint(0, 1)
            if coin == 1:
                how_many += 1
        counts[how_many] += 1
    result = {}
    for key, value in counts.items():
        if key < 1:
            new_value = 0
        else:
            new_value = round((value / 10000) * 100, 2)
        result[key] = new_value
    return result
flip_coin()
