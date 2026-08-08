import random


def flip_coin():
    flip_data = {i: 0 for i in range(11)}

    for _ in range(10000):
        head_count = 0

        for _ in range(10):
            if random.randint(1, 2) == 1:
                head_count += 1
        flip_data[head_count] += 1

    return {key: value / 100 for key, value in flip_data.items()}
