import random
import numpy as np
import matplotlib.pyplot as pit


def flip_coin() -> dict:
    heads_dict = {key: 0 for key in range(11)}
    for _ in range(10000):
        heads = [random.randint(0, 1) for _ in range(10)]
        heads_dict[heads.count(1)] += 1

    return {
        key: round((value / 10000) * 100, 2)
        for key, value in heads_dict.items()
    }


def draw_gaussian_distribution_graph() -> None:
    heads_dict = flip_coin()
    x_data = np.array(list(range(11)))
    y_data = np.array([heads_dict[i] for i in range(11)])

    pit.plot(x_data, y_data)

    pit.title("Gaussian distribution")
    pit.xlabel("Heads count")
    pit.ylabel("Drop percentage %")

    pit.xlim(0, 10)
    pit.ylim(0, 100)

    pit.show()
