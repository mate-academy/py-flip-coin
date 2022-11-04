import random

import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result = {
        0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0
    }
    for i in range(10000):
        count = 0
        for _ in range(10):
            if random.randint(0, 1):
                count += 1
        result[count] += 1
    for key, value in result.items():
        result[key] = value / 100
    return result


def draw_gaussian_distribution_graph(result: dict) -> None:
    pos_head = [x for x in result]
    percent = [y for y in result.values()]
    plt.axis([0, 10, 0, 100])
    plt.yticks([step for step in range(0, 101, 10)])
    plt.xticks([step for step in range(0, 11)])
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.plot(pos_head, percent, color="b")
    plt.show()
