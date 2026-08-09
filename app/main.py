import matplotlib.pyplot as plt
import random
from collections import Counter


def flip_coin(n_cases: int = 10000) -> Counter:
    results = [sum(random.choices((0, 1), k=10)) for _ in range(n_cases)]
    counts = Counter(results)

    return {k: round((counts[k] / n_cases) * 100, 2) for k in range(11)}


print(flip_coin(20000))


def draw_gaussian_distribution_graph(distribution: dict[int, float]) -> None:
    x_values = list(range(11))
    y_values = [distribution.get(k, 0) for k in x_values]
    plt.figure(figsize=(8, 5))

    plt.bar(
        x_values, y_values, color="skyblue",
        edgecolor="black",
        alpha=0.7,
        label="Simulated %"
    )
    # лінія поверх стовпчиків
    plt.plot(x_values, y_values, marker="o", color="darkblue", label="Trend")
    # підписи та сітка
    plt.xlabel("Number of heads (out of 10)")
    plt.ylabel("Percentage (%)")
    plt.title("Distribution of heads in 10 coin flips")
    plt.xticks(x_values)  # показати всі цінності 0..10 по осі x
    plt.grid(axis="y", linestyle="--", alpha=0.4)
    plt.legend()
    plt.tight_layout()
    plt.show()


# Приклад використання
dist = flip_coin(20000)
draw_gaussian_distribution_graph(dist)
