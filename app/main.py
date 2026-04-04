import random
import matplotlib.pyplot as plt


def flip_coin(num_experiments: int = 10000) -> dict:
    results = {i: 0 for i in range(11)}

    for _ in range(num_experiments):
        heads_count = 0

        for _ in range(10):
            if random.choice(["H", "T"]) == "H":
                heads_count += 1

        results[heads_count] += 1

    for key in results:
        results[key] = round(results[key] / num_experiments * 100, 2)

    return results


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()

    heads_counts = list(data.keys())
    percentages = list(data.values())

    plt.figure()
    plt.plot(heads_counts, percentages)
    plt.xlabel("Number of Heads (0-10)")
    plt.ylabel("Percentage (%)")
    plt.title("Distribution of Heads in 10 Coin Flips")
    plt.show()
