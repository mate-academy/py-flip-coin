import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    results = {i: 0 for i in range(11)}

    trials = 10000
    flips_per_trial = 10

    for _ in range(trials):
        heads_count = 0

        for _ in range(flips_per_trial):
            if random.choice(["heads", "tails"]) == "heads":
                heads_count += 1

        results[heads_count] += 1

    for raw_count in results:
        results[raw_count] = (results[raw_count] / trials) * 100

    return results


print(flip_coin())


def draw_gaussian_distribution_graph(distribution: dict) -> None:
    x_value = list(distribution.keys())
    y_value = list(distribution.values())

    plt.bar(x_value, y_value)

    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")

    plt.show()


dist = flip_coin()
draw_gaussian_distribution_graph(dist)

