import random
from collections import defaultdict
from typing import Dict, List
import matplotlib.pyplot as plt


# Функция для симуляции подбрасывания монеты
def flip_coin() -> Dict[int, float]:
    """
    Симулирует 10,000 экспериментов по подбрасыванию монеты 10 раз.
    Возвращает словарь, где ключи — количество орлов (0-10),
    а значения — процент случаев с таким количеством орлов.
    """
    head_counts: defaultdict[int, int] = defaultdict(int)

    # Количество экспериментов
    num_cases: int = 10000

    # Количество подбрасываний монеты в одном эксперименте
    num_flips: int = 10

    # Проводим 10,000 экспериментов
    for _ in range(num_cases):
        # Подбрасываем монету 10 раз и считаем количество орлов
        heads: int = sum(random.choice([0, 1]) for _ in range(num_flips))
        # Увеличиваем счетчик для соответствующего числа орлов
        head_counts[heads] += 1

    # Преобразуем количество случаев в проценты
    for key in head_counts:
        head_counts[key] = (head_counts[key] / num_cases) * 100

    # Убеждаемся, что все возможные значения (0-10) присутствуют в словаре
    for i in range(11):
        if i not in head_counts:
            head_counts[i] = 0.0

    # Сортируем словарь по ключам
    sorted_head_counts: Dict[int, float] = dict(sorted(head_counts.items()))

    return sorted_head_counts


# Функция для построения графика распределения
def draw_gaussian_distribution_graph() -> None:
    """
    Строит график распределения количества орлов при подбрасывании монеты.
    Использует данные из функции flip_coin.
    """
    # Получаем данные из функции flip_coin
    head_counts: Dict[int, float] = flip_coin()

    # Извлекаем ключи (количество орлов) и значения (проценты)
    num_heads: List[int] = list(head_counts.keys())
    percentages: List[float] = list(head_counts.values())

    # Строим столбчатую диаграмму
    plt.bar(num_heads, percentages, color="blue")

    # Добавляем подписи осей и заголовок
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage")
    plt.title("Gaussian Distribution of Coin Flips")

    # Отображаем график
    plt.show()


# Выводим результат работы функции flip_coin
if __name__ == "__main__":
    print(flip_coin())
    draw_gaussian_distribution_graph()
