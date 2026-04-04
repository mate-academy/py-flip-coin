import random


def flip_coin() -> dict[int, float]:
    """Flip a coin 10 times, 10000 experiments, return heads distribution."""
    results: dict[int, int] = {i: 0 for i in range(11)}
    for _ in range(10000):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        results[heads_count] += 1
    return {k: v / 10000 * 100 for k, v in results.items()}


def draw_gaussian_distribution_graph(results: dict[int, float]) -> None:
    import matplotlib.pyplot as plt

    heads = list(results.keys())
    percentages = list(results.values())

    plt.bar(heads, percentages)
    plt.xlabel('Number of heads')
    plt.ylabel('Percentage (%)')
    plt.title('Coin flip distribution')
    plt.show()
