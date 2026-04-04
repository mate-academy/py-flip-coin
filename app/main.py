import random


def flip_coin() -> dict[int, float]:
    attempts = 10000
    counts = {i: 0 for i in range(11)}

    for _ in range(attempts):
        heads = sum(random.choice(["H", "T"]) == "H" for _ in range(10))
        counts[heads] += 1

    return {heads: round(count / attempts * 100, 2) for heads, count in counts.items()}


def draw_gaussian_distribution_graph(distribution: dict[int, float]) -> None:
    import matplotlib.pyplot as plt

    heads = list(distribution.keys())
    probabilities = list(distribution.values())

    plt.bar(heads, probabilities, color="blue")
    plt.xlabel("Number of Heads in 10 Flips")
    plt.ylabel("Probability (%)")
    plt.title("Distribution of Heads in 10 Coin Flips")
    plt.xticks(heads)
    plt.grid(axis="y")

    plt.show()
