from random import choice
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result_count = {}
    total_simulating = 10000

    for _ in range(total_simulating):
        orel_count = sum(1 for _ in range(10)
                         if choice(("orel", "reshka")) == "orel")

        result_count[orel_count] = result_count.get(orel_count, 0) + 1

    percents = {
        key: round((value / total_simulating) * 100, 2)
        for key, value in sorted(result_count.items())
    }
    return percents


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()
    x_coords = list(data.keys())
    y_coords = list(data.values())

    plt.plot(x_coords, y_coords, linestyle="-", color="blue")

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.ylim(0, 100)
    plt.xticks(x_coords)
    plt.grid(axis="y", linestyle="--")
    plt.show()
