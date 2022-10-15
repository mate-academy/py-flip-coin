import random

import matplotlib as mpl
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    flips_rate = {number: 0 for number in range(11)}

    for _ in range(10000):
        count = 0
        for _ in range(10):
            if random.choice(["Head", "Tail"]) == "Head":
                count += 1

        flips_rate[count] += 1

    return {key: value / 100 for key, value in flips_rate.items()}


def draw_gaussian_distribution_graph() -> None:
    dpi = 80
    fig, ax = plt.subplots(dpi=dpi, figsize=(512 / dpi, 384 / dpi))
    mpl.rcParams.update({"font.size": 10})

    plt.axis([0, 10, 0, 100])
    plt.xticks(range(11))
    plt.yticks(range(0, 101, 5))
    plt.setp(ax.yaxis.get_ticklabels()[1::2], visible=False)

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    result = flip_coin()

    plt.plot(result.keys(), result.values(), color="blue", linestyle="solid")
    fig.savefig("graph.png")
