import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict[int: float]:
    coin_sides = ["head", "tail"]
    cases = 10000
    result_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0,
                   5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}

    for case in range(cases):
        times = 10
        heads_count = 0
        for time in range(times):
            side_name = random.choice(coin_sides)
            if side_name == "head":
                heads_count += 1
        result_dict[heads_count] += 1

    for key, value in result_dict.items():
        result_dict[key] = value / cases * 100

    return result_dict


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()
    xpoints = np.array(list(data.keys()))
    ypoints = np.array(list(data.values()))

    # font1 = {"family": "serif", "color": "red", "size": 18}
    # font2 = {"family": "serif", "color": "blue", "size": 14}

    plt.title("Gaussian distribution", loc="center")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.plot(xpoints, ypoints)

    plt.xticks(np.arange(0, 101, 1))
    plt.yticks(np.arange(0, 101, 10))

    plt.show()


draw_gaussian_distribution_graph()
