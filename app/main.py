import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    # Словник для підрахунку кількості кожного результату (від 0 до 10)
    results = {i: 0 for i in range(11)}
    # Кількість симуляцій підкидання монети
    num_trials = 10000

    for _ in range(num_trials):
        # Підкидання монети 10 разів
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        # Збільшення лічильника для кількості "гербів"
        results[heads_count] += 1

    # Переведення лічильників у відсотки
    results = {k: (v / num_trials) * 100 for k, v in results.items()}

    return results


def draw_gaussian_distribution_graph(results: dict) -> None:
    x_list = []
    y_list = []
    for key, value in results.items():
        x_list.append(key)
        y_list.append(value)
    x_points = np.array(x_list)
    y_points = np.array(y_list)
    plt.plot(x_points, y_points)
