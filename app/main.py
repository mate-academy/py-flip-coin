import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    coins_flips = [0] * 11
    for _ in range(10000):
        coins_flips[
            sum([random.randint(0, 1) for _ in range(10)])
        ] += 1

    return {
        key: round((value / 10000) * 100, 2)
        for key, value in enumerate(coins_flips)
    }


def draw_gaussian_distribution_graph(coin_flips: dict) -> None:
    plt.plot(coin_flips.keys(), coin_flips.values())

    plt.ylim(0, 100)

    plt.title("Gaussian Distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()
