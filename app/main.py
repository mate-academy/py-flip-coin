import random
import matplotlib.pyplot as plt


def flip_coin(trials: int = 10000,
              flips_per_trial: int = 10
              ) -> dict[int, float]:
    results = {k: 0 for k in range(0, flips_per_trial + 1)}

    for _ in range(trials):
        heads = 0
        for _ in range(flips_per_trial):
            if random.random() < 0.5:
                heads += 1
        results[heads] += 1

    for heads_count in results:
        results[heads_count] = round(results[heads_count] / trials * 100, 2)

    return results


def draw_gaussian_distribution_graph(dist: dict[int, float]) -> None:
    heads_counts = sorted(dist.keys())
    percentages = [dist[count] for count in heads_counts]

    plt.figure(figsize=(8, 5))
    plt.plot(heads_counts, percentages, color="blue")
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.xticks(heads_counts)
    plt.grid(True, linestyle="--", alpha=0.3)

    plt.show()
