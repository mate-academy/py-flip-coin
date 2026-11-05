import random
import matplotlib.pyplot as plt
from cycler import cycler


def flip_coin() -> dict[int, float]:
    number_of_trials = 10000
    flips_per_trial = 10
    counts = {heads: 0 for heads in range(flips_per_trial + 1)}

    for _ in range(number_of_trials):
        heads_count = sum(
            random.choice([0, 1])
            for _ in range(flips_per_trial))
        counts[heads_count] += 1

    results = {heads: round((count / number_of_trials) * 100, 2)
               for heads, count in counts.items()}
    return results


def draw_gaussian_distribution_graph() -> None:
    result = flip_coin()

    color = plt.get_cmap("Pastel2").colors
    color_cycle = cycler("color", color)
    plt.rc("axes", prop_cycle=color_cycle)

    plt.plot(list(result.keys()), list(result.values()))
    plt.ylabel("Drop Percentage %")
    plt.xlabel("Heads count")
    plt.title("Gaussian distribution")
    plt.ylim(0, 100)
    plt.xlim(0, 10)
    plt.show()


if __name__ == "__main__":
    draw_gaussian_distribution_graph()
