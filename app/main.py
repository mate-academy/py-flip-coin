import random
import matplotlib.pyplot as plt


def flip_coin(num_flips: int = 10, num_trials: int = 10000) -> dict:
    """
    Імітує підкидання монети задану кількість разів
    для заданої кількості експериментів.

    Args:
        num_flips (int): Кількість підкидань монети в одному експерименті.
        num_trials (int): Кількість експериментів.

    Returns:
        dict: Словник, де ключі - кількість випадань герба (0-10),
        а значення - відсоток випадань.
    """

    results = {}
    for _ in range(num_trials):
        heads_count = 0
        for _ in range(num_flips):
            if random.random() < 0.5:  # Імітація герба
                heads_count += 1
        if heads_count not in results:
            results[heads_count] = 0
        results[heads_count] += 1

    percentages = {k: (v / num_trials) * 100 for k, v in results.items()}
    return percentages


def draw_gaussian_distribution_graph(results: dict) -> None:
    """
    Малює графік розподілу результатів підкидання монети.

    Args:
        results (dict): Словник з результатами
        підкидання монети (отриманий з flip_coin).
    """

    x_values = list(results.keys())
    y_values = list(results.values())

    plt.bar(x_values, y_values)
    plt.xlabel("Кількість випадань герба")
    plt.ylabel("Відсоток")
    plt.title("Розподіл результатів підкидання монети")
    plt.xticks(range(11))
    plt.show()


# Виклик функцій
results = flip_coin()
print(results)
draw_gaussian_distribution_graph(results)
