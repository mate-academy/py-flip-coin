import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result_dict = {}
    dict_amount_heads = {}

    # initialize dicts
    for i in range(11):
        result_dict[i] = 0
        dict_amount_heads[i] = 0

    # flip the coins, 1 is "heads"
    for _ in range(10000):
        count_heads = 0
        for _ in range(10):
            count_heads += random.randint(0, 1)
        dict_amount_heads[count_heads] += 1

    # calc percentage
    for key, value in dict_amount_heads.items():
        result_dict[key] = dict_amount_heads[key] * 100 / 10000

    return result_dict


def draw_gaussian_distribution_graph(data: dict) -> None:
    x_points = []
    y_points = []
    for key, value in data.items():
        x_points.append(key)
        y_points.append(value)

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage, %")
    plt.plot(x_points, y_points)
    plt.show()
