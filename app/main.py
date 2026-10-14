import random
import matplotlib.pyplot as plt


def flip_coin() -> dict[int, float]:
    result = dict.fromkeys(range(11), 0)
    for i in range(10000):
        heads = 0
        for one_coin in range(10):
            if random.choice([0, 1]) == 1:
                heads += 1
        result[heads] += 1

    for key in result:
        result[key] = round(result[key] / 100, 2)
    return result


def draw_gaussian_distribution_graph(data: dict[int, float]) -> None:
    x_point = data.keys()
    y_point = data.values()
    plt.plot(x_point, y_point)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.xlim(0, 10)
    plt.ylim(0, 100)
    plt.show()


draw_gaussian_distribution_graph(flip_coin())
