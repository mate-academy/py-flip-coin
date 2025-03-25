from enum import IntEnum
import random

import matplotlib.pyplot as plt


class Coin(IntEnum):
    TAILS = 0
    HEADS = 1


def flip_coin(
    trials: int = 10_000,
    flips_per_trial: int = 10
) -> dict[int, float]:
    counts_by_heads = {
        count: 0 for count in range(flips_per_trial + 1)
    }

    for _ in range(trials):
        heads_count = sum(
            random.getrandbits(1) == Coin.HEADS
            for _ in range(flips_per_trial)
        )
        counts_by_heads[heads_count] += 1

    percentage_by_heads = {
        count: round(frequency / trials * 100, 2)
        for count, frequency in counts_by_heads.items()
    }

    return percentage_by_heads


def draw_gaussian_distribution_graph(
    trials: int = 10_000,
    flips_per_trial: int = 10,
    save_to_file: str | None = None
) -> None:
    percentage_by_heads = flip_coin(
        trials=trials, flips_per_trial=flips_per_trial
    )

    head_counts = list(percentage_by_heads.keys())
    head_percentages = list(percentage_by_heads.values())

    plt.plot(head_counts, head_percentages, color="blue")
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.xticks(head_counts)
    plt.yticks(
        range(0, int(max(head_percentages)) + 10, 5)
    )
    plt.grid(True)

    if save_to_file:
        plt.savefig(save_to_file, dpi=300)
    else:
        plt.show()


if __name__ == "__main__":
    draw_gaussian_distribution_graph()
