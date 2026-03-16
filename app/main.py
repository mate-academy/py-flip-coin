import random
from matplotlib import pyplot as plt


def flip_coin() -> dict:
    flip_dict = {amount: 0 for amount in range(11)}
    for _ in range(10000):
        head = 0
        for _ in range(10):
            flip = random.randint(0, 1)
            if flip == 0:
                head += 1
        flip_dict[head] += 1
    result_dict = {amount: round((flip_dict[amount] / 10000) * 100, 2)
                   for amount in range(11)}
    return result_dict


def draw_gaussian_distribution_graph() -> None:
    x = list(flip_coin().keys)
    y = list(flip_coin().values)
    plt.plot(x, y)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage%")
    plt.title("Gaussian distribution")
    plt.show()
