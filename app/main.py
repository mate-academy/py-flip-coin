import matplotlib.pyplot as plt
import random


def flip_coin() -> dict:
    eagle_dict = {i: 0 for i in range(11)}
    for experiment in range(10000):
        heads = sum(random.randint(0, 1) for _ in range(10))
        eagle_dict[heads] += 1
    for keys in eagle_dict:
        eagle_dict[keys] = eagle_dict[keys] / 10000 * 100
    return eagle_dict


result = flip_coin()


def draw_gaussian_distribution_graph(eagle_dict: dict) -> None:
    x_graph = eagle_dict.keys()
    y_graph = eagle_dict.values()
    plt.plot(x_graph, y_graph, marker="o")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.xlim(0, 10)
    plt.ylim(0, 100)
    plt.title("Gaussian distribution")
    plt.show()


draw_gaussian_distribution_graph(result)
