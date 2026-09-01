import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result_dict = {i: 0 for i in range(11)}
    for attempt in range(10000):
        heads_counter = 0
        for i in range(1, 11):
            if random.randint(0, 1) == 1:
                heads_counter += 1
        result_dict[heads_counter] = result_dict[heads_counter] + 1
    for key, value in result_dict.items():
        result_dict[key] = round((value / 10000) * 100, 2)
    return result_dict


def draw_gaussian_distribution_graph(result_dict: dict) -> None:
    x_list = []
    y_list = []
    for key, value in result_dict.items():
        x_list.append(key)
        y_list.append(value)
    plt.plot(x_list, y_list)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()
