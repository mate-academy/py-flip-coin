import random
import numpy as np
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    res_dict = {}
    # Список для збереження результатів
    results = []
    for _ in range(10000):
        # Лічильник гербів
        heads_count = 0
        for _ in range(10):  # 10 разів
            # Вибираємо нуль як герби
            if random.choice([0, 1]) == 0:
                heads_count += 1
        results.append(heads_count)

    # Записуємо в словник ключі -герби 0-10, значення - кількість 0-10 в списку
    for number in sorted(results):
        if number not in res_dict:
            res_dict[number] = (sorted(results).count(number) / 10000) * 100

    # точки x, y для графіку
    x_ls = list(res_dict.keys())
    y_ls = list(res_dict.values())
    x_points = np.array(x_ls)
    y_points = np.array(y_ls)

    plt.plot(x_points, y_points)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage")

    return res_dict
