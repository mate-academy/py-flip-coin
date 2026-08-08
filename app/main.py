import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    def toss_coin_10_times() -> int:
        heads_count = 0
        for _ in range(10):
            if random.choice([0, 1]):
                heads_count += 1
        return heads_count

    times = 10_000
    results = dict.fromkeys(range(11), 0.0)
    for count in range(times):
        heads = toss_coin_10_times()
        results[heads] += 1

    for key in results:
        results[key] = round(results[key] / times * 100, 2)

    return results


def draw_gaussian_distribution_graph() -> None:
    results = flip_coin()
    x_axis = results.keys()
    y_axis = results.values()
    plt.title("Distribution of heads in 10 coin tosses")
    plt.xlabel("Number of heads")
    plt.ylabel("Percentage (%)")
    plt.plot(x_axis, y_axis)
    plt.show(block=True)
