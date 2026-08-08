import random
import matplotlib.pyplot as plt


def flip_coin() -> dict[int, float]:
    trials = 10000
    flips = 10

    head_counts = {i: 0 for i in range(11)}

    for _ in range(trials):
        heads = sum(random.randint(0, 1) for _ in range(flips))
        head_counts[heads] += 1

    percentages = {
        head_number: round((head_count / trials) * 100, 2)
        for head_number, head_count in head_counts.items()
    }

    return percentages


def draw_gaussian_distribution_graph() -> None:
    percentages = flip_coin()

    head_numbers = list(percentages.keys())
    percentages_values = list(percentages.values())

    plt.plot(head_numbers, percentages_values)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")
    plt.show()
