import numpy as np
import random
import matplotlib.pyplot as plt
from typing import Dict


def flip_coin(num_trials: int = 10000) -> Dict[int, float]:
    results = [sum(random.randint(0, 1)
                   for _ in range(10)) for _ in range(num_trials)]
    counts = [results.count(i) for i in range(11)]
    percentages = [count / num_trials * 100 for count in counts]
    return dict(zip(range(11), percentages))


def draw_gaussian_distribution_graph() -> None:
    variable_x = np.arange(0, 11)
    mu = 5
    sigma = 2
    variable_y = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(
        -(variable_x - mu) ** 2 / (2 * sigma ** 2)
    )

    plt.figure(figsize=(10, 6))
    plt.plot(variable_x, variable_y * 100)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")
    plt.grid()
    plt.show()


print(flip_coin())
draw_gaussian_distribution_graph()
