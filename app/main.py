import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    coin = (0, 1)
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
                   10: 0
                   }

    for _ in range(10000):
        num_of_heads = [random.choice(coin) for _ in range(10)].count(0)
        result_dict[num_of_heads] += 0.01

    return result_dict


def draw_gaussian_distribution_graph(result_dict: dict) -> None:
    x_points = result_dict.keys()
    y_points = result_dict.values()

    plt.plot(x_points, y_points)
    plt.title("Gaussian distributeion")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.grid()
    plt.show()


draw_gaussian_distribution_graph(flip_coin())
