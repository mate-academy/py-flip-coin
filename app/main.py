import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin(trials=10000):
    results = {i: 0 for i in range(11)}

    for _ in range(trials):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        results[heads_count] += 1

    for count in results:
        results[count] = round((results[count] / trials) * 100, 2)

    return results

def draw_gaussian_distribution_graph(distribution_dict) -> None:
    x = np.array(list(distribution_dict.keys()))
    y = np.array(list(distribution_dict.values()))
    plt.plot(x, y)

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()


distribution = flip_coin()
print(distribution)
draw_gaussian_distribution_graph(distribution)