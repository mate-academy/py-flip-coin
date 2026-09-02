import random
from matplotlib import pyplot


def flip_coin() -> dict:

    coin = ["heads", "tails"]

    heads_dict = {
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

    for _ in range(0, 10000):
        heads_count = 0

        for _ in range(0, 10):
            step = random.choice(coin)
            if step == "heads":
                heads_count += 1

        heads_dict[heads_count] += 1

    for key, value in heads_dict.items():
        heads_dict[key] = value * 100 / 10000

    return heads_dict


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()
    x_cord = data.keys()
    y_cord = data.values()

    pyplot.plot(x_cord, y_cord)
    pyplot.show()
