import random
from typing import Dict

import matplotlib.pyplot as plt


def flip_coin() -> Dict[int, float]:
    trials_count: int = 10000
    # Инициализируем словарь: ключи (0-10), значения (количество выпадений)
    results: Dict[int, int] = {heads: 0 for heads in range(11)}

    for _ in range(trials_count):
        # Подсчитываем количество орлов в серии из 10 бросков
        heads_count: int = sum(random.random() < 0.5 for _ in range(10))
        results[heads_count] += 1

    # Возвращаем словарь, где значения пересчитаны в проценты
    return {
        heads: (count / trials_count) * 100
        for heads, count in results.items()
    }


def draw_gaussian_distribution_graph(data: Dict[int, float]) -> None:
    # Разделяем ключи и значения для построения осей графика
    heads_counts: list = list(data.keys())
    percentages: list = list(data.values())

    plt.plot(heads_counts, percentages)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    # Настройка осей для соответствия визуальному образцу
    plt.xticks(range(11))
    plt.ylim(0, 100)
    plt.xlim(0, 10)

    plt.show()
