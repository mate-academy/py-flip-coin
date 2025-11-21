import matplotlib.pyplot as plt
import random


def flip_coin() -> dict:
    result = {i: 0 for i in range(0, 11)}
    for _ in range(10000):
        heads = 0
        for _ in range(10):
            if random.randint(0, 1) == 1:
                heads += 1
        result[heads] += 1
    for index in result:
        result[index] = round((result[index] / 10000) * 100, 2)
    return result


print(flip_coin())


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()
    xsa = list(data.keys())
    ysa = list(data.values())
    plt.xlabel("Number of heads")
    plt.ylabel("Percentage (%)")
    plt.plot(xsa, ysa)
    plt.xticks(xsa)
    plt.show()


draw_gaussian_distribution_graph()
