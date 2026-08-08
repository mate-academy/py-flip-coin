import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    stats = {i: 0 for i in range(11)}
    for _ in range(10000):
        current_heads = sum(random.randint(0, 1) for _ in range(10))
        stats[current_heads] += 1
    stats = {k: (v / 10000) * 100 for k, v in stats.items()}
    return stats


def draw_gaussian_distribution_graph() -> None:
    temp = flip_coin()

    x_values = sorted(temp.keys())
    y_values = [temp[key] for key in x_values]

    plt.figure(figsize=(8, 6))

    # Будуємо синю лінію, як на твоєму прикладі
    plt.plot(x_values, y_values, color="blue", linewidth=2)

    # Налаштовуємо осі відповідно до картинки
    plt.xlim(0, 10)
    plt.ylim(0, 100)  # Максимальне значення на осі Y — 100%
    plt.xticks(range(11))

    # Назви осей та заголовка
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.grid(True, which="both", linestyle=":", alpha=0.3)
    plt.show()
