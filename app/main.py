import random
from datetime import datetime


def flip_coin() -> dict:
    results = {
        0 : 0,
        1 : 0,
        2 : 0,
        3 : 0,
        4 : 0,
        5 : 0,
        6 : 0,
        7 : 0.0,
        8 : 0.0,
        9 : 0.0,
        10 : 0.0
    }

    nb_tests = 20000
    for _ in range(nb_tests + 1):
        current_time = datetime.now()
        random.seed(datetime.timestamp(current_time))

        head = 0
        for flip in range(0, 10):
            if random.randint(1, 2) == 1:
                head += 1

        results[head] += 1 / nb_tests

    for key in results:
        results[key] = round(100 * results[key], 2)

    return results
