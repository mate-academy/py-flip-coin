import random
import matplotlib.pyplot as plt


def flip_coin() -> dict[int, float]:
    num_cases = 10000
    results = {i: 0 for i in range(11)}

    for _ in range(num_cases):
        heads = sum(random.choice([0, 1]) for _ in range(10))
        results[heads] += 1

    # Convert counts to percentages
    for key in results:
        results[key] = (results[key] / num_cases) * 100

    return results


def draw_gaussian_distribution_graph(results: dict[int, float]) -> None:
    plt.bar(results.keys(), results.values())
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian Distribution of Coin Flips")
    plt.show()
