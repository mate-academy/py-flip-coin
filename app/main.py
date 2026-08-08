import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    probability = dict(zip(range(11), [0] * 11))
    for _ in range(10000):
        count = sum([1 for _ in range(10)
                     if random.choice(["heads", "tails"]) == "heads"])
        probability[count] += 1 / 100
    return probability


def draw_gaussian_distribution_graph(data: dict) -> None:
    plt.plot(data.keys(), data.values())
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.ylim(0, 100)
    plt.yticks(range(0, 101, 10))
    plt.xlim(0, 10)
    plt.grid()
    plt.show()
