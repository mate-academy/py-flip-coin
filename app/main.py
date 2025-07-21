import random
from matplotlib import pyplot


def flip_coin() -> dict:
    result_dict = {i: 0 for i in range(11)}
    for _ in range(10000):
        head = sum(random.choice([0, 1]) for _ in range(10))
        result_dict[head] += 1
    for res in result_dict:
        result_dict[res] = round(result_dict[res] / 100, 2)
    return result_dict


def draw_gaussian_distribution_graph() -> None:
    need_result = flip_coin()
    x_coordinate = [key for key in need_result.keys()]
    y_coordinate = [percentage for percentage in need_result.values()]
    pyplot.plot(x_coordinate, y_coordinate)
    pyplot.title("Gaussian distribution")
    pyplot.xlabel("Heads count")
    pyplot.ylabel("Drop percentage %")

    pyplot.show()
