import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    statistic = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0,
                 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
    for _ in range(10000):
        results = [random.choice(["heads", "tails"]) for _ in range(10)]
        results_heads = results.count("heads")
        statistic[results_heads] += 1
    for result in statistic:
        statistic[result] = statistic[result] / 100
    return statistic


def draw_gaussian_distribution_graph(statistic: dict) -> None:
    y_points = list(statistic.values())
    x_points = list(statistic.keys())
    plt.plot(x_points, y_points)
    plt.show()
