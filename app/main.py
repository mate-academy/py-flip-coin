import random
import matplotlib.pyplot as plt


def flip_coin(cases: int = 10000) -> dict:
    heads_count = {heads_drop: 0 for heads_drop in range(11)}

    for case in range(cases):
        heads_dropped_in_case = 0

        for flip in range(10):
            if random.random() < 0.5:
                heads_dropped_in_case += 1

        heads_count[heads_dropped_in_case] += 1

    result = {}

    for heads, count in heads_count.items():
        percentage = (count / cases) * 100
        result[heads] = round(percentage, 2)

    return result


def draw_gaussian_distribution_graph() -> None:
    graph_data = flip_coin(10000)
    x_data = list(graph_data.keys())
    y_data = list(graph_data.values())
    plt.plot(x_data, y_data)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
