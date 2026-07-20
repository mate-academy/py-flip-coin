import random
import matplotlib.pyplot as plt


def flip_coin(num_trials: int = 10000) -> dict:
    results = {i: 0 for i in range(11)}

    for _ in range(num_trials):
        heads_count = 0
        for _ in range(10):
            if random.randint(0, 1) == 1:
                heads_count += 1
        results[heads_count] += 1

    percentages = {
        key: round(value / num_trials * 100, 2)
        for key, value in results.items()
    }

    return percentages


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()

    plt.bar(data.keys(), data.values())
    plt.xlabel("Кількість орлів")
    plt.ylabel("Відсоток випадків (%)")
    plt.title("Розподіл кількості орлів при 10 підкиданнях монетки")
    plt.show()


if __name__ == "__main__":
    print(flip_coin())
    draw_gaussian_distribution_graph()
