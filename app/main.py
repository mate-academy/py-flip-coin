import random
import matplotlib.pyplot as plt
from collections import defaultdict


def flip_coin(num_simulations: int = 10000) -> dict[int, float]:
    """
    Симулює підкидання монети 10 разів у кожному
    з num_simulations експериментів.

    Повертає словник, де ключі — це кількість 'орлів', а значення — відсоток,
    з якою ця кількість випадала серед усіх експериментів.
    """
    results = defaultdict(int)
    for _ in range(num_simulations):
        heads_count = sum(random.randint(0, 1) for _ in range(10))
        results[heads_count] += 1

    distribution = {
        count: round(amount / num_simulations * 100, 2)
        for count, amount in results.items()
    }

    for heads in range(11):
        distribution.setdefault(heads, 0.0)

    return distribution


def draw_gaussian_distribution_graph(distribution: dict[int, float]) -> None:
    """
    Малює графік Гаусового (нормального)
    розподілу на основі словника з розподілом.
    """
    head_counts = sorted(distribution.keys())
    drop_percentages = [distribution[count] for count in head_counts]

    plt.plot(head_counts, drop_percentages, "blue")
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    result = flip_coin()
    print(result)
    draw_gaussian_distribution_graph(result)
