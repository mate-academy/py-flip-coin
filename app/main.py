import random
import matplotlib.pyplot as plt


def flip_coin(trials: int = 10000, flips: int = 10) -> dict[int, float]:
    results: dict[int, int] = {i: 0 for i in range(flips + 1)}

    for _ in range(trials):
        heads = sum(random.choice([0, 1]) for _ in range(flips))
        results[heads] += 1

    for key in results:
        results[key] = round((results[key] / trials) * 100, 2)

    return results


def draw_gaussian_distribution_graph(data: dict[int, float]) -> None:
    plt.bar(data.keys(), data.values(), color="skyblue", edgecolor="black")
    plt.title("Gaussian (Binomial) Distribution of Coin Flips")
    plt.xlabel("Кількість орлів у 10 підкиданнях")
    plt.ylabel("Відсоток випадків (%)")
    plt.xticks(range(0, 11))
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()


if __name__ == "__main__":
    distribution = flip_coin()
    print(distribution)
    draw_gaussian_distribution_graph(distribution)
