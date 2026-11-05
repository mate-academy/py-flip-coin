from random import choice
import matplotlib.pyplot as plt


def flip_coin() -> dict[int, float]:
    results = {i: 0 for i in range(11)}

    for _ in range(10000):
        heads_count = 0

        for _ in range(10):
            if choice(["heads", "tails"]) == "heads":
                heads_count += 1

        results[heads_count] += 1

    return {
        key: round(value / 10000 * 100, 2)
        for key, value in results.items()
    }


def draw_gaussian_distribution_graph() -> None:
    results = flip_coin()
    x_axis = list(results.keys())
    y_axis = list(results.values())

    plt.ylim(0, 100)
    plt.plot(x_axis, y_axis, marker="o")

    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")

    plt.xticks(range(11))
    plt.ylim(0, 100)

    plt.show()
