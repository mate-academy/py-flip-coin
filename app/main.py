import random

import matplotlib.pyplot as plt


def flip_coin(
    trials: int = 10000,
    flips_per_trial: int = 10,
) -> dict[int, float]:
    counts = {i: 0 for i in range(flips_per_trial + 1)}

    for _ in range(trials):
        heads = sum(random.choice([0, 1]) for _ in range(flips_per_trial))
        counts[heads] += 1

    percentages = {k: round(v / trials * 100, 2) for k, v in counts.items()}
    return percentages


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()

    keys = list(data.keys())
    values = list(data.values())

    plt.figure(figsize=(10, 6))

    plt.bar(
        keys, values,
        color="skyblue",
        edgecolor="black",
        label="Результат симуляції",
    )

    plt.plot(
        keys, values,
        color="red",
        marker="o",
        linestyle="-",
        linewidth=2,
    )

    title = (
        "Розподіл Гауса: кількість орлів "
        "при 10 підкиданнях монети"
    )
    plt.title(title, fontsize=14, fontweight="bold")
    plt.xlabel("Кількість орлів", fontsize=12)
    plt.ylabel("Відсоток (%)", fontsize=12)
    plt.xticks(keys)
    plt.grid(axis="y", alpha=0.5, linestyle="--")
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    result = flip_coin()
    print(result)

    draw_gaussian_distribution_graph()
