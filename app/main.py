import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result_dict = {0: 0,
                   1: 0,
                   2: 0,
                   3: 0,
                   4: 0,
                   5: 0,
                   6: 0,
                   7: 0,
                   8: 0,
                   9: 0,
                   10: 0}
    coin = ["heads", "tails"]
    for _ in range(10000):
        count = 0
        for _ in range(10):
            if random.choice(coin) == "heads":
                count += 1
        result_dict[count] += 1
    for key, value in result_dict.items():
        result_dict[key] = round(value / 10000 * 100, 2)
    return result_dict


def draw_gaussian_distribution_graph() -> None:
    result = flip_coin()
    x_cord = result.keys()
    y_cord = result.values()
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage, %")
    plt.plot(x_cord, y_cord)
    plt.xlim(0, 10)
    plt.ylim(0, 100)
    plt.show()
