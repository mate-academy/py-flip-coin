import random
import matplotlib.pyplot as plt


def flip_coin() -> None:
    cases = 10000
    result_counts = {}
    for i in range(11):
        result_counts[i] = 0

    for _ in range(cases):
        heads_in_this_serie = 0
        for _ in range(10):
            flip = random.randint(0, 1)
            if flip == 1:
                heads_in_this_serie += 1
        result_counts[heads_in_this_serie] += 1

    result_percent = {}

    for key, value in result_counts.items():
        result_percent[key] = round((value / cases) * 100, 2)
    return result_percent


def draw_gaussian_distribution_graph(data: dict) -> None:

    heads_count = list(data.keys())
    drop_percentage_percent = list(data.values())
    plt.plot(heads_count, drop_percentage_percent, color="blue")
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.xticks(range(11))
    plt.show()


results = flip_coin()


draw_gaussian_distribution_graph(results)
