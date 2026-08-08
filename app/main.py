import random
import matplotlib.pyplot as plt


def flip_coin(options: list = ["heads", "tails"]) -> dict:
    heads_count_dict = {
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
    count_heads = 0
    for _ in range(10000):
        for _ in range(10):
            result = random.choice(options)
            if result == "heads":
                count_heads += 1
        heads_count_dict[count_heads] += 1
        count_heads = 0
    return {key: (value / 100) for key, value in heads_count_dict.items()}


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()
    coord_x = data.keys()
    coord_y = data.values()

    plt.bar(coord_x, coord_y)

    plt.xlabel("Heads numbers (in 10 flips)")
    plt.ylabel("Percentual (%)")
    plt.title("Gaussian Distribution - 10.000 simulation cases")

    plt.grid(axis="y", alpha=0.3)

    plt.show()


draw_gaussian_distribution_graph()
