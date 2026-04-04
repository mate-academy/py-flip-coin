import math
import random
from matplotlib import pyplot as plt
import numpy as np


def flip_coin(number_of_trials: int = 10000) -> dict[int, float]:
    dict_result = {i: 0 for i in range(11)}
    for _ in range(number_of_trials):
        value = sum(random.randint(0, 1) for _ in range(10))
        dict_result[value] += 1
    for key in dict_result:
        dict_result[key] = round(dict_result[key] / number_of_trials * 100, 2)
    return dict_result


def draw_gaussian_distribution_graph(data: dict[int, float]) -> None:
    x_bar = list(data.keys())
    y_bar = list(data.values())
    plt.bar(x_bar, y_bar, width=0.6, color="C0", alpha=0.7)
    (plt.xlabel("Number of heads"),
     plt.ylabel("Percentage(%)"),
     plt.title("Bar_of_pain"))
    n_smth = 10
    p_smth = 0.5
    mu = n_smth * p_smth
    sigma = math.sqrt(n_smth * p_smth * (1 - p_smth))
    x_smooth = np.linspace(min(x_bar), max(x_bar), 200)
    gaussian_pdf = ((1 / (sigma * np.sqrt(2 * np.pi)))
                    * np.exp(-(x_smooth - mu)**2 / (2 * sigma**2)))
    scale_pdf = gaussian_pdf * 100
    plt.plot(x_smooth, scale_pdf, color="C1", linewidth=2)
    plt.xticks(x_bar)
    plt.legend(["Gaussian approx", "Simulated"])
    plt.grid(True, linestyle="--", alpha=0.4)
    plt.tight_layout()
    plt.show()
