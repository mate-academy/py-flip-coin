import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result = dict.fromkeys(range(11), 0)
    total = 10000
    for _ in range(total):
        heads = 0
        for _ in range(10):
            heads += random.randint(0, 1)
        result[heads] += 1
    for key, value in result.items():
        result[key] = round(value / total * 100, 2)
    return result


def draw_gaussian_distribution_graph() -> None:
    graph = flip_coin()
    plt.plot(graph.keys(), graph.values(), color="blue")
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.ylim(0, 100)
    plt.xticks(range(0, 11))
    plt.show()
