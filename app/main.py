import random


def flip_coin() -> dict:
    done_dict = {i: 0 for i in range(11)}
    for _ in range(10000):  # Виконуємо 10000 експериментів
        counter = 0  # Обнуляємо лічильник для кожної серії підкидань
        for _ in range(10):  # Підкидаємо монету 10 разів
            flip = random.randint(0, 1)  # Генеруємо випадкове число (0 або 1)
            if flip == 1:
                counter += 1  # Збільшуємо лічильник, якщо випала голова
        done_dict[counter] += 1  # Оновлюємо словник

    # Перетворюємо значення в проценти
    for key in done_dict:
        done_dict[key] = round((done_dict[key] / 10000) * 100, 2)

    return done_dict
