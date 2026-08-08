import random
# import numpy as np
# import matplotlib.pyplot as plt


def throw_coin_ten_times() -> int:
    heads = 0
    for _ in range(10):
        if random.randint(0, 1) == 1:
            heads += 1
    return heads


def flip_coin() -> dict:
    total = 10000
    result = {}
    result_counts = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0
    }
    for _ in range(total):
        key = throw_coin_ten_times()
        result_counts[key] += 1

    for key, value in result_counts.items():
        percent = (value / total) * 100
        result[key] = round(percent, 2)

    # draw_gaussian_distribution_graph(result)
    return result


"""
def draw_gaussian_distribution_graph(result: dict) -> None:
    keys = []
    values = []
    for key, value in result.items():
        keys.append(key)
        values.append(value)

    print("KEYS: ", keys, "VALUES: ", values)
    o_x = np.array(keys)
    o_y = np.array(values)

    plt.plot(o_x, o_y)

    plt.title("Gaussian distribution")
    plt.xlabel("Head count")
    plt.ylabel("Drop percentage %")

    plt.show()
"""
