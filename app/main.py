import random


def flip_coin() -> dict[int, float]:
    cases = 10_000
    flips_per_case = 10
    counts = dict.fromkeys(range(flips_per_case + 1), 0)

    for _ in range(cases):
        heads = sum(
            random.randint(0, 1)
            for _ in range(flips_per_case)
        )
        counts[heads] += 1

    return {
        heads: round(count / cases * 100, 2)
        for heads, count in counts.items()
    }


def draw_gaussian_distribution_graph() -> None:
    import matplotlib.pyplot as plt

    distribution = flip_coin()

    plt.plot(
        list(distribution.keys()),
        list(distribution.values()),
        marker="o",
    )
    plt.xlabel("Number of heads in 10 flips")
    plt.ylabel("Percentage of trials (%)")
    plt.title("Coin toss distribution")
    plt.xticks(range(11))
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    print(flip_coin())
    draw_gaussian_distribution_graph()
