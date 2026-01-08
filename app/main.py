import random


def flip_coin() -> dict:
    result = {i: 0 for i in range(11)}

    num_trials = 10000
    for _ in range(num_trials):
        num_heads = 0
        for _ in range(10):
            if random.random() < 0.5:
                num_heads += 1
        result[num_heads] += 1

    percentage = {
        key: (value / num_trials) * 100 for key, value in result.items()
    }

    return percentage
