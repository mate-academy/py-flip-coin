import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    heads_or_tail = ["head", "tail"]

    total_cases = 10_000
    result_choice = {i: 0 for i in range(11)}

    for _ in range(total_cases):
        count = 0
        for i in range(10):
            if random.choice(heads_or_tail) == "head":
                count += 1

        result_choice[count] += 1

    result = {}

    for pick, count in result_choice.items():
        percent = round((count / total_cases) * 100, 2)
        result[pick] = percent

    return result


def draw_gaussian_distribution_graph() -> None:
    result_dict = flip_coin()

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    x_points = np.array([pick for pick in result_dict.keys()])
    y_points = np.array([percent for percent in result_dict.values()])
    plt.ylim(0, 100)

    plt.plot(x_points, y_points)
    plt.show()
