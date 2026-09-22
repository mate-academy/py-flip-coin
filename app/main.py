import random
import numpy as np
import matplotlib.pyplot as plt


from matplotlib.ticker import MultipleLocator


def flip_coin() -> dict:
    result = {numb: 0 for numb in range(11)}

    for _ in range(10000):
        total_heads_by_attempt = 0
        for _ in range(10):
            total_heads_by_attempt += random.randint(0, 1)
        result[total_heads_by_attempt] += 1

    return {
        num: round(res / 10000 * 100, 2)
        for num, res in result.items()
    }


def draw_gaussian_distribution_graph() -> None:
    datas = flip_coin()

    a_x = np.array(list(datas.keys()))
    a_y = np.array(list(datas.values()))

    _, ax = plt.subplots()
    ax.plot(a_x, a_y)
    ax.yaxis.set_minor_locator(MultipleLocator(5))
    ax.yaxis.set_major_locator(MultipleLocator(10))

    plt.xlim(0, len(a_x) - 1)
    plt.ylim(0, 100)

    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")

    plt.show()
