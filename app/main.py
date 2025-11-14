import random
import matplotlib.pyplot as plt


def flip_coin(num_cases: int = 10000) -> dict:
    counts = {}
    for heads in range(11):
        counts[heads] = 0

    for _ in range(num_cases):
        num_heads = 0
        for _ in range(10):
            if random.randint(0, 1) == 1:
                num_heads += 1
        counts[num_heads] += 1

    percentage_distribution = {}

    for heads, count in counts.items():
        percentage = (count / num_cases) * 100
        percentage_distribution[heads] = round(percentage, 2)
    return percentage_distribution


def draw_gaussian_distribution_graph(data: dict[int, float]) -> None:
    """Rysuje wykres rozkładu wyników."""
    x_values = list(data.keys())
    y_values = list(data.values())

    plt.bar(
        x_values,
        y_values, color="skyblue",
        edgecolor="black"
    )
    plt.title("Rozkład liczby orłów przy 5 rzutach monetą")
    plt.xlabel("Liczba orłów (heads)")
    plt.ylabel("Procent (%)")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()
