import random
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("TkAgg")


def flip_coin() -> dict:
    coin_dict = {
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
        10: 0,
    }
    for _ in range(10000):
        count_eagle = 0
        for i in range(0, 10):
            random_value = random.randint(0, 1)
            if random_value == 1:
                count_eagle += 1
        coin_dict[count_eagle] += 1

    for key in coin_dict:
        coin_dict[key] = round((coin_dict[key] / 10000) * 100, 2)

    return coin_dict


def draw_gaussian_distribution_graph() -> None:
    dct = flip_coin()
    x_line = np.array(list(dct.keys()))
    y_line = np.array(list(dct.values()))

    plt.plot(x_line, y_line)

    plt.title("Gaussian Distribution")
    plt.xlabel("Drop percentage %")
    plt.ylabel("Calorie Burnage")

    plt.ylim(0, 100)

    plt.show()
