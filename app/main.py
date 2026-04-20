import random
from collections import Counter
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    list_with_variant = ["heads", "tails"]
    result_dict = {}
    for _ in range(10000):  # 10 000 експериментів
        result_of_flip_coin = [
            random.choice(list_with_variant)
            for _ in range(10)
        ]
        result_dict_of_ten_flip = Counter(result_of_flip_coin)
        heads_count = result_dict_of_ten_flip.get("heads", 0)
        result_dict[heads_count] = result_dict.get(heads_count, 0) + 1

    # Перетворюємо у відсотки
    for key in result_dict:
        result_dict[key] = round(result_dict[key] / 10000 * 100, 2)

    return result_dict


# Отримуємо дані для осей
xline = list(flip_coin().keys())  # кількість орлів
yline = list(flip_coin().values())  # відсотки

# Створюємо графік
plt.bar(xline, yline, color="skyblue", edgecolor="black")

# Підписи осей і заголовок
plt.xlabel("Кількість орлів (heads) із 10 підкидань")
plt.ylabel("Відсоток (%)")
plt.title("Розподіл кількості 'heads' у 10 підкиданнях монети")

# Відображаємо графік
plt.show()
