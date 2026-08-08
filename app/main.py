import random


def flip_coin() -> dict:
    result = {}
    for value in range(11):
        result[value] = 0
    for _ in range(10000):
        count = 0
        for _ in range(10):
            throw = random.choice(["tail", "head"])
            if throw == "head":
                count += 1
        result[count] += 1

    lista = []
    for key, value in result.items():
        percent = (value / 10000) * 100
        result[key] = round(percent, 2)
        lista.append(result.get(key))

    return result
