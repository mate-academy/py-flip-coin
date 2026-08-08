import random
import matplotlib.pyplot as plt


TRIALS = 10_000
FLIPS = 10


def flip_coin() -> dict:
    flip_counts = {}

    for flip in range(0, 11):
        flip_counts[flip] = 0

    for _ in range(TRIALS):
        heads_count = 0

        for _ in range(FLIPS):
            if random.random() < 0.5:
                heads_count += 1

        flip_counts[heads_count] += 1

    for key in flip_counts:
        flip_counts[key] = round(flip_counts[key] * 100 / TRIALS, 2)

    return flip_counts


def draw_gaussian_distribution_graph(distribution: dict[int, float]) -> None:
    x_coordinate = list(distribution.keys())
    y_coordinate = list(distribution.values())

    plt.plot(
        x_coordinate, y_coordinate, color="blue"
    )

    plt.xlabel(
        "Heads count"
    )
    plt.ylabel(
        "Drop percentage %"
    )
    plt.title(
        "Gaussian Distribution"
    )

    plt.xticks(x_coordinate)
    plt.yticks(range(0, 101, 10))
    plt.ylim(0, 100)

    plt.show()


if __name__ == "__main__":
    distribution_result = flip_coin()
    draw_gaussian_distribution_graph(distribution_result)
