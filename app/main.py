import random
import matplotlib.pyplot as plt


def flip_coin(num_trials: int = 10000, num_flips: int = 10) -> dict:
    result_dict: dict[int, float] = dict.fromkeys(range(11), 0)

    for trial in range(num_trials):
        heads_count = 0

        for flips in range(num_flips):
            flips_result = random.randint(0, 1)

            if flips_result == 1:
                heads_count += 1

        result_dict[heads_count] += 1

    for key, value in result_dict.items():
        percentage_value = (value / num_trials) * 100
        result_dict[key] = round(percentage_value, 2)

    return result_dict


def draw_gaussian_distribution_graph(data: dict) -> None:
    x_points = list(data.keys())
    y_points = list(data.values())

    plt.plot(x_points, y_points)
    plt.xlabel("heads count")
    plt.ylabel("percentage, %")
    plt.title("LOOK AT THIS GRAPH")

    plt.show()


draw_gaussian_distribution_graph(flip_coin())
