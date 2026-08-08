import random
import numpy as np
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    parcelling_result = dict.fromkeys([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0)
    number_of_attempts = 10000

    for i in range(0, number_of_attempts):
        number_of_heads_choice = 0
        for ten_att in range(0, 10):
            number_of_heads_choice += random.randint(0, 1)
        parcelling_result[number_of_heads_choice] += 1
    return {
        key: value * 100 / number_of_attempts for key,
        value in parcelling_result.items()
    }


def draw_gaussian_distribution_graph() -> None:
    x_coord = np.array([value for value in range(1, 11)])
    y_coord = np.array(
        [value for key, value in flip_coin().items() if key != 0]
    )

    plt.plot(x_coord, y_coord)

    plt.xlabel("Number of heads")
    plt.ylabel("Percentage of chance")

    plt.show()
