import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    coin = {i: 0 for i in range(11)}  # от 0 до 10 орлов
    trials = 10000

    for _ in range(trials):
        heads = 0
        for _ in range(10):
            if random.choice(["H", "T"]) == "H":
                heads += 1
        coin[heads] += 1

    # Преобразуем в проценты
    for key in coin:
        coin[key] = round((coin[key] / trials) * 100, 2)

    return coin


def draw_gaussian_distribution_graph() -> None:
    # Дані для графіка
    x_range = np.arange(0, 11)
    y_range = np.exp(-((x_range - 5) ** 2) / 10) * 100
    fig, ax = plt.subplots()
    ax.plot(x_range, y_range, color="blue")
    # Додавання мінорних тиків
    ax.minorticks_on()
    # Налаштування основних і мінорних тиків
    ax.xaxis.set_major_locator(plt.MultipleLocator(1))
    ax.xaxis.set_minor_locator(plt.MultipleLocator(0.5))
    ax.yaxis.set_major_locator(plt.MultipleLocator(10))
    ax.yaxis.set_minor_locator(plt.MultipleLocator(5))
    # Налаштування сітки
    ax.grid(which="both", linestyle="--", linewidth=0.5)
    # Назви осей і заголовок
    ax.set_xlabel("Heads count")
    ax.set_ylabel("Drop percentage %")
    ax.set_title("Gaussian distribution")
    plt.show()
