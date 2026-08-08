import random


def flip_coin() -> dict:
    # Проводимо не менше 10000 підкидань монети
    num_flips = 10000
    num_heads_count = [0] * 11  # Масив для підр кі голів у випад кіль викидів
    for _ in range(num_flips):
        # Проводимо 10 підкидань монети
        num_heads = sum([random.choice([0, 1]) for _ in range(10)])
        num_heads_count[num_heads] += 1

    # Обчислюємо відсоток для кожної кількості голів
    result_dict = {}
    for num_heads, count in enumerate(num_heads_count):
        result_dict[num_heads] = round(count / num_flips * 100, 2)

    return result_dict


results = flip_coin()
print(results)
