import random


def flip_coin() -> dict:
    count = {i : 0 for i in range(11)}
    for num in range(10000):
        heads = 0
        for i in range(10):
            random_num = random.randint(0, 1)
            if random_num == 1:
                heads += 1
        count[heads] += 1
    return {key: round(value / 10000 * 100, 2) for key, value in count.items()}
