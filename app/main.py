import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result = []
    for i in range(10000):
        eagle = 0
        for coin in range(10):
            coin_side = random.randint(0, 1)
            if coin_side == 1:
                eagle += 1
        result.append(eagle)
    final = {}
    for heads in range(11):
        final[heads] = round(result.count(heads) / 10000 * 100, 2)
    return final


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()
    plt.bar(data.keys(), data.values())
    plt.xlabel("Number of heads")
    plt.ylabel("Percentage")
    plt.title("Gaussian Distribution")
    plt.show()
