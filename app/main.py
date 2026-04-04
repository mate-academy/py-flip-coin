# import random

# def flip_coin() -> dict:
#     result_dict ={}
#     head = 1
#     back = 2
#     for _ in range(1000):
#         for _ in range(10):
#             variable = random.randint(1, 3)
#             if variable == 1:
#                 result_dict[head] += 1
#
#     total =

import random


def flip_coin() -> dict:
    result_dict = {i: 0 for i in range(11)}
    # Створюємо словник для збереження
    # кількості "heads" для кожного можливого випадку
    # {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}

    for _ in range(10000):
        heads_count = 0
        for _ in range(10):
            if random.random() < 0.5:
                # Імітуємо кидок монети з ймовірністю "орла" 50%
                heads_count += 1
        result_dict[heads_count] += 1
        # Оновлюємо значення словника для відповідної кількості "heads"

    # Розраховуємо відсоток для кожної кількості "heads"
    total_experiments = 10000
    for key in result_dict:
        result_dict[key] = (result_dict[key] / total_experiments) * 100

    return result_dict


print(flip_coin())


result_dict = {i: 0 for i in range(11)}
print(result_dict)


# Якщо ви підкинете монету, у 50% випадків випадуть орли2 рази?
#
# Напишіть функцію flip_coin, яка проводить не менше
# 10000 випадків підкидання монети 10 разів.
# Він має повернути dict, де ключі — це кількість
# можливих викинутих орлів (від 0 до 10),
# а значення — відсоток того, скільки це число
# випало з усіх випадків.
#
# print(flip_coin())
# # {0: 0,13, 1: 0,97, 2: 4,22, 3: 12,04, ... }
# Якщо ви зробили все правильно, ви повинні зауважити,
# що найбільший відсоток кількості випали голів
# знаходиться приблизно в середині, 4-6 разів і прагне до 0,
# коли мова йде про краї 0-1 і 9-10.
# Це називається нормальним розподілом або розподілом Гауса
