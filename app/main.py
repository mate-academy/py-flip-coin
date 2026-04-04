import random
from matplotlib import pyplot as plt
from collections import Counter


def flip_coin() -> dict:
    count_heads = []
    for _ in range(10_000):
        count_heads.append(
            sum([random.choice([0, 1]) for _ in range(10)])
        )
    count_mapping = Counter(count_heads)
    return {
        key: round(value / 10_000 * 100, 2)
        for key, value in count_mapping.items()
    }


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()

    x_coord = list(data.keys())
    y_coord = list(data.values())

    plt.figure()
    plt.plot(x_coord, y_coord, marker="o")
    plt.xlabel("Number of heads in 10 flips")
    plt.ylabel("Percentage")
    plt.title("Coin flip distribution 10 000 experiments")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    print(flip_coin())
