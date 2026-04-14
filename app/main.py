import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    trials = 10000
    flips_per_trial = 10

    results = {i: 0 for i in range(flips_per_trial + 1)}

    for _ in range(trials):

        heads: int = sum(random.choices([0, 1], k=flips_per_trial))
        results[heads] += 1

    percentage_results = {}
    for heads_count, times_dropped in results.items():
        percentage = round((times_dropped / trials) * 100, 2)
        percentage_results[heads_count] = percentage

    return percentage_results


def draw_gaussian_distribution_graph() -> None:

    data = flip_coin()

    x_values = list(data.keys())
    y_values = list(data.values())

    plt.plot(x_values, y_values)

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.xticks(range(11))
    plt.yticks(range(0, 101, 10))

    plt.xlim(0, 10)
    plt.ylim(0, 100)

    plt.show()
