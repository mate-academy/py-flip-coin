import random


def flip_coin() -> dict[int, float]:
    trials = 10000
    results = {i: 0 for i in range(11)}

    for _ in range(trials):
        heads_count = 0

        for _ in range(10):
            if random.choice(["H", "T"]) == "H":
                heads_count += 1

        results[heads_count] += 1

    for key in results:
        results[key] = round(results[key] / trials * 100, 2)

    return results


def draw_gaussian_distribution_graph(data: dict[int, float]) -> None:
    import matplotlib.pyplot as plt

    x_keys = list(data.keys())
    y_values = list(data.values())

    plt.figure(figsize=(8, 5))
    plt.bar(x_keys, y_values)

    plt.xlabel("Number of heads (0–10)")
    plt.ylabel("Percentage (%)")
    plt.title("Distribution of Heads in 10 Coin Flips")

    plt.xticks(range(11))

    plt.grid(axis="y", linestyle="--", alpha=0.7)

    plt.show()


if __name__ == "__main__":
    data = flip_coin()
    draw_gaussian_distribution_graph(data)
