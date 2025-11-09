import random
import matplotlib.pyplot as plt


def flip_coin(
    trials: int = 10000,
    flips_per_trial: int = 10,
) -> dict[int, float]:
    """
    Симулирует подбрасывание монеты и возвращает распределение количества орлов.

    Args:
        trials (int): количество серий подбрасываний монеты.
        flips_per_trial (int): количество подбрасываний в каждой серии.

    Returns:
        dict[int, float]: словарь, где ключ — количество орлов (0–10),
        значение — процент случаев из общего числа.
    """
    results = {i: 0 for i in range(flips_per_trial + 1)}

    for _ in range(trials):
        heads = sum(random.choice([0, 1]) for _ in range(flips_per_trial))
        results[heads] += 1

    for key in results:
        results[key] = round(results[key] / trials * 100, 2)

    return results


def draw_gaussian_distribution_graph(data: dict[int, float]) -> None:
    """
    Строит график распределения (похожий на нормальное распределение).

    Args:
        data (dict[int, float]): словарь с результатами подбрасываний.
    """
    x_values = list(data.keys())
    y_values = list(data.values())

    plt.plot(x_values, y_values, color="blue")
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    distribution = flip_coin()
    print(distribution)
    draw_gaussian_distribution_graph(distribution)
