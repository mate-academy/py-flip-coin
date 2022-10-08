import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    res_dict = {i: 0 for i in range(10)}
    for i in range(10001):
        flipping = [random.randint(0, 1) for _ in range(10)].count(1)
        res_dict.update({flipping: res_dict.get(flipping, 0) + 1})
        if not flipping:
            res_dict.update({0: res_dict.get(0, 0) + 1})
    all_cases = sum(res_dict.values())
    for key, item in res_dict.items():
        res_dict.update({key: round(item / all_cases * 100, 2)})
    return res_dict


def draw_gaussian_distribution_graph(flip: dict) -> None:
    x_axis = flip.keys()
    y_axis = flip.values()
    plt.plot(x_axis, y_axis)
    plt.axis([0, 10, 0, 100])
    plt.title("Flip coins")
    plt.xlabel("Dropped")
    plt.ylabel("Percent")
    plt.plot(x_axis, y_axis, color="g", linewidth=3)
    plt.show()
