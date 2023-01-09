import random

import matplotlib.pyplot as plt


def flip_coin() -> dict:
    total_list = [
        [random.choice(["H", "T"]) for _ in range(10)]
        for _ in range(10000)
    ]
    count_heads = [chance.count("H") for chance in total_list]
    percentage_heads = {i: count_heads.count(i) / 100 for i in range(11)}
    return percentage_heads


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()
    dpi = 80
    fig = plt.figure(dpi=dpi, figsize=(512 / dpi, 384 / dpi))
    plt.axis([0, 10, 0, 100])
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage%")
    plt.plot(data.keys(), data.values())
    fig.savefig("fig.png")
    plt.show()


if __name__ == "__main__":
    print(draw_gaussian_distribution_graph())
