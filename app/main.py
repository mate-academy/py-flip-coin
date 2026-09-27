import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    results = {i: 0 for i in range(11)}

    for _ in range(10000):
        heads_count = sum(random.randint(0, 1) for _ in range(10))
        results[heads_count] += 1

    return {k: v / 100 for k, v in results.items()}


def draw_gaussian_distribution_graph() -> None:
    results = flip_coin()

    plt.bar(list(results.keys()), list(results.values()))
    plt.xlabel("Кількість гербів")
    plt.ylabel("Відсоток")
    plt.title("Normal Distribution")
    plt.show()
