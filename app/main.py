import random
import matplotlib.pyplot as plt


def flip_coin() -> dict[int, float]:
    trials = 10000
    results = {i: 0 for i in range(11)}

    for _ in range(trials):
        heads = sum(random.choice([0, 1]) for _ in range(10))
        results[heads] += 1

    for key in results:
        results[key] = round(results[key] / trials * 100, 2)

    return results


def draw_gaussian_distribution_graph() -> None:
    distribution = flip_coin()
    head_counts = list(distribution.keys())
    percentages = list(distribution.values())

    plt.figure(figsize=(10, 6))
    plt.plot(head_counts, percentages, marker="o", linestyle="-", color="blue")
    plt.title("Gaussian Distribution of Coin Flips (10 flips per trial)")
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage of Occurrence")
    plt.grid(True)
    plt.xticks(range(11))
    plt.show()


if __name__ == "__main__":
    print(flip_coin())
    draw_gaussian_distribution_graph()
