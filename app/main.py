import random


def flip_coin():
    result_dict = {}
    count_dict = {}
    for i in range(1, 10001):
        suma = 0
        for _ in range(10):
            suma += random.randint(0, 1)
        count_dict[suma] = count_dict.get(suma, 0) + 1
    num = sum(count_dict.values())
    for k, v in count_dict.items():
        result_dict[k] = v / num * 100
    return result_dict
