import random


def flip_coin() -> dict:
    cases = 10000
    results = {heads: 0 for heads in range(11)}

    for _ in range(cases):
        heads = 0

        for _ in range(10):
            if random.choice([True, False]):
                heads += 1

        results[heads] += 1

    return {
        heads: round(count / cases * 100, 2)
        for heads, count in results.items()
    }


def draw_gaussian_distribution_graph() -> None:
    import matplotlib.pyplot as plt

    distribution = flip_coin()

    plt.bar(distribution.keys(), distribution.values())
    plt.xlabel("Number of heads")
    plt.ylabel("Percentage")
    plt.title("Coin Flip Distribution")
    plt.xticks(range(11))
    plt.show()
