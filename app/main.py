from random import randint
from matplotlib import pyplot as plt


def flip_coin() -> dict:
    dict_of_probabilities = {
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
    tries = 10000
    for _ in range(tries):
        count_head = 0
        for _ in range(10):
            head = randint(0, 1)
            if head == 1:
                count_head += 1
        dict_of_probabilities[count_head] += 1
    return {
        number: count / tries * 100
        for number, count in dict_of_probabilities.items()
    }


def draw_gaussian_distribution_graph() -> None:
    special_dict = flip_coin()
    x_points = [number for number in special_dict]
    y_points = [number for number in special_dict.values()]

    plt.plot(x_points, y_points)
    plt.show()
