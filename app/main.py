import random
from collections import Counter
import matplotlib.pyplot as plt


def flip_coin(total_flips: int) -> dict:
    list_of_flipping = []
    for _ in range(total_flips):
        list_of_flipping.append(
            sum(random.randint(0, 1) for _ in range(10)))
    counter = Counter(list_of_flipping)
    result = {}
    for i in range(11):
        result[i] = round((counter[i] / total_flips) * 100, 2)
    return result


def draw_gaussian_distribution_graph(distribution: dict) -> None:
    keys = sorted(distribution.keys())
    values = [distribution[k] for k in keys]

    plt.figure(figsize=(10, 5))
    plt.plot(keys, values, linestyle='-', color='blue', label='Heads distribution')
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage (%)")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.xticks(range(11))
    plt.show()


result_dict = flip_coin(10000)
draw_gaussian_distribution_graph(result_dict)
