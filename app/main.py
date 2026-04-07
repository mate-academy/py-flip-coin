import random
from collections import Counter
from math import comb
import matplotlib.pyplot as plt


def flip_coin(
    n_cases: int = 100_000,
    flips_per_case: int = 10,
) -> dict[int, float]:
    """
    Run n_cases experiments of flipping a fair coin flips_per_case times.
    Return {k: percentage_of_cases_with_exactly_k_heads} for k in [0..n].
    """
    counts = Counter()
    for _ in range(n_cases):
        heads = sum(random.getrandbits(1) for _ in range(flips_per_case))
        counts[heads] += 1
    return {
        k: round(100 * counts.get(k, 0) / n_cases, 2)
        for k in range(flips_per_case + 1)
    }


def draw_gaussian_distribution_graph(
    dist: dict[int, float],
    save_as: str | None = None,
) -> None:
    """
    Plot the distribution (percent) over number of heads.
    If save_as is provided, save the figure to that path.
    """
    xs = sorted(dist.keys())
    ys = [dist[x] for x in xs]

    plt.figure(figsize=(7, 4.5))
    plt.plot(xs, ys, marker="o")
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Percentage %")
    plt.ylim(0, max(ys) * 1.2 if ys else 1)
    plt.grid(True, axis="y", alpha=0.3)

    if save_as:
        plt.savefig(save_as, dpi=150, bbox_inches="tight")
    plt.show()


def exact_probability_percent(n_flips: int, k_heads: int) -> float:
    return comb(n_flips, k_heads) / (2 ** n_flips) * 100


if __name__ == "__main__":
    dist = flip_coin(n_cases=200_000, flips_per_case=10)
    print(dist)

    draw_gaussian_distribution_graph(
        dist,
        save_as="gaussian_distribution.png",
    )

    p5 = exact_probability_percent(10, 5)
    p2 = exact_probability_percent(10, 2)
    print(f"Exact P(5 heads in 10 flips): {p5: .5f}%")
    print(f"Exact P(2 heads in 10 flips): {p2: .5f}%")
