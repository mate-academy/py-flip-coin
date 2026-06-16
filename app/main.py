import random
import matplotlib.pyplot as plt


EXPERIMENTS_COUNT = 10000
FLIPS_PER_ROUND = 10


def flip_coin_one_time() -> str:
    return random.choice(["heads", "tails"])


def flip_coin_one_round(attempts: int) -> int:
    heads_count = 0

    for _ in range(attempts):
        flip_result = flip_coin_one_time()
        if flip_result == "heads":
            heads_count += 1

    return heads_count


def flip_coin_n_rounds(attempts: int) -> dict[int, float]:
    results_count = {}

    for _ in range(attempts):
        heads_count = flip_coin_one_round(FLIPS_PER_ROUND)
        results_count[heads_count] = results_count.get(heads_count, 0) + 1

    results_percentage = {
        heads_count: (count / attempts) * 100
        for heads_count, count in results_count.items()
    }

    return results_percentage


def flip_coin() -> dict[int, float]:
    return flip_coin_n_rounds(EXPERIMENTS_COUNT)


def draw_gaussian_distribution_graph() -> None:
    experiments_results = flip_coin()
    sorted_experiments_results = sorted(experiments_results.items())

    xpoints = []
    ypoints = []

    for key, value in sorted_experiments_results:
        xpoints.append(key)
        ypoints.append(value)

    plt.plot(xpoints, ypoints)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage, %")
    plt.title("Gaussian distribution")
    plt.show()
