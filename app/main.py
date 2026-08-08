import random
from collections import defaultdict
import matplotlib.pyplot as plt


def flip_coin(trials: int = 10000) -> dict[int, float]:
    """
    Симулирует 10 бросков монеты `trials` раз.
    Возвращает словарь {количество орлов: процент случаев}.
    """
    heads_counts = defaultdict(int)

    for _ in range(trials):
        # 0 = решка, 1 = орел
        heads_total = sum(random.choice([0, 1]) for _ in range(10))
        heads_counts[heads_total] += 1

    percentages = {heads_number: (count / trials * 100)
                   for heads_number, count in heads_counts.items()}

    # Добавляем отсутствующие значения от 0 до 10
    for heads_number in range(11):
        percentages.setdefault(heads_number, 0.0)

    # Сортируем по ключу
    return dict(sorted(percentages.items()))


def draw_gaussian_distribution_graph(distribution: dict[int, float]) -> None:
    """
    Строит график распределения выпадений орлов.
    """
    num_heads_list = list(distribution.keys())
    percentages_list = list(distribution.values())

    plt.figure(figsize=(8, 5))
    plt.bar(num_heads_list, percentages_list, color="skyblue",
            edgecolor="black")
    plt.xlabel("Количество орлов в 10 бросках")
    plt.ylabel("Процент случаев (%)")
    plt.title("Распределение количества орлов при 10 бросках монеты")
    plt.xticks(range(11))
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()
