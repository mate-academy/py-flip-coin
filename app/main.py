from random import randint
import matplotlib.pyplot as plt


def flip_coin() -> dict:

    counter = 0
    list_of_heads = []

    for ten_flips in range(10000):
        counter = 0

        for flip in range(10):
            coin = randint(1, 2)
            if coin == 1:
                counter += 1

        list_of_heads.append(counter)

    gaussian_dict = {
        i: round(list_of_heads.count(i) / 10000 * 100, 2)
        for i in range(11)
    }
    draw_gaussian_distribution_graph(gaussian_dict)
    return gaussian_dict


def draw_gaussian_distribution_graph(gau_dict: dict) -> None:
    x_point = gau_dict.keys()
    y_point = gau_dict.values()
    plt.bar(x_point, y_point)

    plt.xlabel("Numbers of head dropped")
    plt.ylabel("Percentage of total tries")

    plt.show()
