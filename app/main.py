import random
import matplotlib.pyplot as plt


def flip_coin(trials: int = 10000) -> dict[int, float]:
    if trials <= 0:
        raise ValueError("trials must be > 0")
    results = {i: 0 for i in range(11)}
    for _ in range(trials):
        heads = sum(random.getrandbits(1) for _ in range(10))
        results[heads] += 1
    return {k: round(v / trials * 100, 2) for k, v in results.items()}


def draw_gaussian_distribution_graph(dist: dict[int, float]) -> None:
    x = list(dist.keys())
    y = list(dist.values())  # % values
    plt.bar(x, y)
    plt.xlabel('Number of heads')
    plt.ylabel('Percentage')
    plt.title('Distribution of heads in 10 coin flips')
    plt.show()
