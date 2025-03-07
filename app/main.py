import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    results = {i: 0 for i in range(11)}

    for _ in range(10000):
        head_count = sum(random.choice([0, 1]) for _ in range(10))
        results[head_count] += 1
    head_percentages = \
        {key: (val / 10000) * 100 for key, val in results.items()}
    return head_percentages


def draw_gaussian_distribution_graph() -> None:
    plt.ylim(0, 100)
    plt.xlim(0, 10)
    plt.xlabel("Number of Heads")
    plt.ylabel("Drop Percentage (%)")

    heads_percentage = flip_coin()

    drop_percentage_points: [float] = [
        percentage for _, percentage in sorted(heads_percentage.items())
    ]

    plt.plot(drop_percentage_points, marker="o")
    plt.title("Heads Count Distribution for Coin Flips")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    draw_gaussian_distribution_graph()
