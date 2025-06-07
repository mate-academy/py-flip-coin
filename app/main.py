import random
import matplotlib.pyplot as plt


def flip_coin(num_experiments: int = 100_000) -> dict[int, float]:
    results = {i: 0 for i in range(11)}  # Від 0 до 10 гербів

    for _ in range(num_experiments):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        results[heads_count] += 1

    # Перетворимо у відсотки
    for count in results:
        results[count] = round((results[count] / num_experiments) * 100, 2)

    return results


def draw_gaussian_distribution_graph(data: dict[int, float]) -> None:
    heads = list(data.keys())
    percentages = list(data.values())

    plt.figure(figsize=(10, 6))
    plt.bar(heads, percentages, color="skyblue", edgecolor="black")
    plt.title("Distribution of Number of Heads in 10 Coin Flips")
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage (%)")
    plt.xticks(range(11))
    plt.grid(axis="percentages", linestyle="--", alpha=0.7)
    plt.show()


if __name__ == "__main__":
    simulation_results = flip_coin()
    print(simulation_results)
    draw_gaussian_distribution_graph(simulation_results)
