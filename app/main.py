import random
import matplotlib.pyplot as plt


def flip_coin(flip: int = 10000) -> dict:
    count_success = 0
    chance_dict = {i: 0 for i in range(11)}
    for _ in range(0, flip):
        for _ in range(0, 10):
            if random.choice([0, 1]) == 1:
                count_success += 1
        chance_dict[count_success] += 1
        count_success = 0
    for key, value in chance_dict.items():
        chance_dict[key] = round((value / flip) * 100, 2)
    return chance_dict


def draw_gaussian_distribution_graph(chance_dict: dict) -> None:
    x_points = list(chance_dict.keys())
    y_points = list(chance_dict.values())
    plt.bar(x_points, y_points)
    plt.title("Gaussian Distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()
