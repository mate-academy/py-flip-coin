import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    counts_eagle = {
        0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0,
        6: 0, 7: 0, 8: 0, 9: 0, 10: 0,
    }
    for _ in range(10000):
        flips = random.choices(["Heads", "Tails"], k=10)
        heads_count = flips.count("Heads")
        counts_eagle[heads_count] += 1
    percent_result = {}
    for key, value in counts_eagle.items():
        result = round(value / 10000 * 100, 2)
        percent_result[key] = result
    return percent_result


def draw_gaussian_distribution_graph() -> None:
    result = flip_coin()
    x_coord = result.keys()
    y_coord = result.values()

    plt.bar(x_coord, y_coord)
    plt.title("Coin flip distribution")
    plt.xlabel("Number of heads")
    plt.ylabel("Percentage")
    plt.show()
