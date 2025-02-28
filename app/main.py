import random
import matplotlib.pyplot as plt


def flip_coin(n_trials: int = 10000) -> dict[int, float]:
    results = {head: 0 for head in range(11)}

    for _ in range(n_trials):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        results[heads_count] += 1

    for key in results:
        results[key] = round((results[key] / n_trials) * 100, 2)

    return results


def draw_gaussian_distribution_graph(data: dict[int, float]) -> None:
    plt.figure(figsize=(8, 5))
    plt.bar(data.keys(), data.values(), color="skyblue", edgecolor="black")
    plt.xlabel("Кількість голів")
    plt.ylabel("Відсоток випадань (%)")
    plt.title("Гаусівський розподіл підкидань монети")
    plt.xticks(range(11))
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()
