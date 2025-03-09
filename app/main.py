import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result_dict = {
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
    for _ in range(10000):
        heads = flip_10()
        result_dict[heads] += 1
    return {
        key: round((value / 10000) * 100, 2)
        for key, value in result_dict.items()
    }


def flip_10() -> int:
    heads_count = 0
    for _ in range(10):
        flipped_coin = random.randint(0, 1)
        if flipped_coin == 0:
            heads_count += 1
    return heads_count


def draw_gaussian_distribution_graph() -> None:
    info_for_graph = flip_coin()
    x_axis = list(info_for_graph.keys())
    y_axis = list(info_for_graph.values())

    plt.plot(x_axis, y_axis, linestyle="-", color="b")
    plt.ylim(0, 100)
    plt.yticks(range(0, 101, 10))

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage")

    plt.legend()
    plt.show()
