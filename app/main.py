import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    head_dict = {i: 0 for i in range(0, 11)}
    count = 10000
    for _ in range(count):
        current_coin_list = [
            random.choice(("head", "tail"))
            for _ in range(10)
        ]
        head_count = current_coin_list.count("head")
        head_dict[head_count] += 1

    for key, value in head_dict.items():
        head_dict[key] = round(value / count * 100, 2)

    return head_dict


def draw_gaussian_distribution_graph(data: dict) -> None:
    plt.plot(data.keys(), data.values())
    plt.ylim(0, 100)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.yticks(range(0, 101, 10))
    plt.xticks(range(0, 11, 1))
    plt.show()


draw_gaussian_distribution_graph(flip_coin())
