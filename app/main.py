import random
import matplotlib.pyplot as plt


def flip_coin(numbers: int = 10000) -> None:
    result_dict = {k: 0 for k in range(11)}

    for _ in range(numbers):
        heads = sum(random.randint(0, 1) for _ in range(10))
        result_dict[heads] += 1

    for key in result_dict:
        result_dict[key] = round(result_dict[key] / numbers * 100, 2)
    return result_dict


def draw_gaussian_distribution_graph(
    result_dict: dict = flip_coin(10000)
) -> plt:
    x_axis = list(result_dict.keys())
    y_axis = list(result_dict.values())
    plt.bar(x_axis, y_axis)
    plt.xlabel("Number of heads")
    plt.ylabel("Percentage")
    plt.title("Distribution of heads in 10 coin flips")
    plt.show()
