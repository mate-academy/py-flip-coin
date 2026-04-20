import random
import matplotlib.pyplot as plt


def flip_coin(trials: int = 10000,
              flips_per_trial: int = 10) -> dict[int, float]:
    """
    Simulate flipping a fair coin multiple times and calculate the percentage
    distribution of how many heads appear in each trial.

    :param trials: number of independent experiments
    :param flips_per_trial: number of flips per experiment
    :return: dict mapping number of heads (0–flips_per_trial) to percentage
    """
    results = {i: 0 for i in range(flips_per_trial + 1)}

    for _ in range(trials):
        heads = sum(random.choice([0, 1]) for _ in range(flips_per_trial))
        results[heads] += 1

    # convert counts to percentages
    for heads_count in results:
        results[heads_count] = round((results[heads_count] / trials) * 100, 2)

    return results


def draw_gaussian_distribution_graph(trials: dict[int, float]) -> None:
    x, y = trials.keys(), trials.values()
    plt.plot(x, y)

    plt.ylim(0, 100)
    # plt.xlim(0, 10)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()


if __name__ == "__main__":
    tr = flip_coin()
    draw_gaussian_distribution_graph(tr)
