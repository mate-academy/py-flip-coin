import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    dicto = {
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
        heads = 0
        for _ in range(10):
            heads += random.randint(0, 1)

        dicto[heads] += 1

    for el in dicto:
        dicto[el] /= 100

    return dicto


def draw_gaussian_distribution_graph(dictus: dict) -> None:
    keys = list(data.keys())
    values = list(data.values())
    plt.plot(keys, values, marker="o", color="blue")
    plt.xlabel("Number of heads")
    plt.ylabel("Percentage (%)")
    plt.title("Gaussian distribution of coin flips")
    plt.grid(True)
    plt.xticks(range(11))
    plt.show()


data = flip_coin()
draw_gaussian_distribution_graph(data)