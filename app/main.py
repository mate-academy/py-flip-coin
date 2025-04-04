import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result = {}
    for _ in range(10000):
        count = 0
        for _ in range(10):
            if random.random() < 0.5:
                count += 1
        result[count] = result.get(count, 0) + 1

    result = dict(sorted(result.items()))

    for key in result.keys():
        result[key] /= 10000
        result[key] *= 100

    return result


def draw_gaussian_distribution_graph(coin_flips: dict) -> None:
    plt.plot(coin_flips.keys(), coin_flips.values())
    plt.xlim(0, 10)
    plt.ylim(0, 100)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()
