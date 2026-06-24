import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    coin_statistics = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0
    }
    coin_flip_variants = ["heads", "tails"]
    for _ in range(10000):
        count = 0
        for i in range(10):
            choice = random.choice(coin_flip_variants)
            if choice == "heads":
                count += 1
        coin_statistics[count] += 1
    return {key: value / 10000 * 100 for key, value in coin_statistics.items()}


distribution = flip_coin()


def draw_gaussian_distribution_graph(distribution: dict) -> None:
    x_label = list(distribution.keys())
    y_label = list(distribution.values())
    plt.plot(x_label, y_label)
    plt.xlabel("Number of heads")
    plt.ylabel("Percentage")
    plt.title("Distribution of coin flips")
    plt.show()
