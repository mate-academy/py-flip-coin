import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:

    result_dict = {i: 0 for i in range(11)}
    number_of_values = 10000

    for i in range(number_of_values):
        eagles = 0
        for _ in range(10):
            if random.randint(0, 1) == 1:
                eagles += 1
        result_dict[eagles] += 1

    for key in result_dict:
        result_dict[key] = round(result_dict[key] / number_of_values * 100, 2)

    return result_dict


def draw_gaussian_distribution_graph(result_dict_for_persentages: dict
                                     ) -> None:
    x_points = result_dict_for_persentages.keys()
    y_points = result_dict_for_persentages.values()
    plt.plot(x_points, y_points)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")
    plt.show()
