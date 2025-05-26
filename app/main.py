import random
import matplotlib.pyplot as plt


def flip_coin() -> dict[int, float]:
    trials = 10000
    results = {i: 0 for i in range(11)}

    for _ in range(trials):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        results[heads_count] += 1

    for key in results:
        results[key] = round((results[key] / trials) * 100, 2)

    return results


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()
    head_counts = list(data.keys())
    probabilities = list(data.values())

    plt.bar(head_counts, probabilities, color="skyblue")
    plt.xlabel("Number of Heads")
    plt.ylabel("Probability (%)")
    plt.title("Gaussian Distribution of Coin Flips")
    plt.show()
