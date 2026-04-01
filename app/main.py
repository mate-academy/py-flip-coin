import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin(times: int = 10000) -> dict:
    answer = {key: 0 for key in range(0, 11)}

    for _ in range(times):
        count = sum(random.randint(0, 1) for _ in range(10))

        answer[count] += 1
    answer = {key: 100 * value / times for key, value in answer.items()}

    return answer


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()
    y_values = np.array(list(data.values()))
    x_keys = np.array(list(data.keys()))

    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")

    plt.ylim(0, 100)
    plt.yticks(range(0, 101, 10))
    plt.xticks(range(0, 11, 1))
    plt.plot(x_keys, y_values)
    plt.show()
