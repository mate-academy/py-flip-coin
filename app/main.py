import random
from matplotlib import pyplot as plt


def draw_gaussian_distribution_graph(
        distribution: dict[int, float]
) -> None:
    x_heads = list(distribution.keys())
    y_percentage = list(distribution.values())

    plt.plot(x_heads, y_percentage)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()


def coin_flip(times: int) -> list[int]:
    flips: list[int] = []
    for _ in range(times):
        flips.append(random.randint(0, 1))
    return flips


def flip_coin() -> dict[int, float]:
    flips_count: int = 10
    cases_count: int = 10000
    coin_flip_map: dict[int, int] = {k: 0 for k in range(flips_count + 1)}

    for _ in range(cases_count):
        flips = coin_flip(flips_count)
        coin_flip_map[flips.count(1)] += 1

    for i in range(flips_count + 1):
        coin_flip_map[i] = round(coin_flip_map[i] / cases_count * 100, 2)

    return coin_flip_map
