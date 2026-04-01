import random

from matplotlib import pyplot as plt


def flip_coin(num_trials: int = 10000) -> dict:
    results = {i : 0 for i in range(11)}
    for trial in range(num_trials):
        eagle = 0
        for inside_trial in range(10):
            if random.random() < 0.5:
                eagle += 1
        results[eagle] += 1
    for num in results:
        results[num] = round(results[num] / num_trials * 100, 2)
    return results


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()
    x_axis = sorted(data.keys())
    y_axis = data.values()
    plt.plot(x_axis, y_axis)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.xticks(range(0, 11, 1))
    plt.yticks(range(0, 101, 10))
    plt.show()
