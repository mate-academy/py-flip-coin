import random


def flip_coin() -> dict:
    run = 0
    result = {i : 0 for i in range(11)}
    total_runs = 10000

    while run < total_runs:
        heads_count = 0
        for i in range(10):
            random_number = random.randint(0, 1)
            if random_number == 0:
                heads_count += 1
        result[heads_count] += 1
        run += 1

    for key in result:
        result[key] = result[key] / total_runs * 100

    return result
