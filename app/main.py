import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    counter = {}

    fliped_coins = [
        [random.randint(0, 1) for _ in range(10)]
        for _ in range(10000)
    ]
    for fliped in fliped_coins:
        if fliped.count(1) not in counter:
            counter[fliped.count(1)] = 1
        else:
            counter[fliped.count(1)] += 1

    percentage = {k: (v / 10000) * 100 for k, v in sorted(counter.items())}

    return percentage


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()
    xpoints = list(data.keys())
    ypoints = list(data.values())

    plt.plot(xpoints, ypoints)

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.xticks(range(0, 11))
    plt.yticks(range(0, 101, 10))
    plt.xlim(0, 10)
    plt.ylim(0, 100)
    plt.show()
