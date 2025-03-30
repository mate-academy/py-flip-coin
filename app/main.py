import random
from matplotlib import pyplot


def flip_coin(num_experiments: int = 10000,
              num_flips: int = 10) -> dict:
    result_dict = {}

    for _ in range(num_experiments):
        num_heads = sum(random.choice([0, 1]) for _ in range(num_flips))
        result_dict[num_heads] = result_dict.get(num_heads, 0) + 1

    for heads in result_dict:
        result_dict[heads] /= num_experiments / 100

    return result_dict


def draw_gaussian_distribution_graph(data: dict) -> None:
    keys, values = zip(*sorted(data.items()))
    pyplot.bar(keys, values, align="center")
    pyplot.xlabel("Number of Heads")
    pyplot.ylabel("Percentage")
    pyplot.title("Gaussian Distribution")
    pyplot.show()
