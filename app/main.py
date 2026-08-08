import random


def flip_coin() -> dict:
    counter = 0
    moneta = ["head", "tail"]
    lista = []
    for number in range(0, 10000):
        lista.append(counter)
        counter = 0
        for number in range(0, 10):
            if random.choice(moneta) == "head":
                counter += 1

    slownik = dict(zip([number for number in range(0, 11)],
                       [0 for number in range(0, 11)]))
    for number in lista:
        if number in slownik:
            slownik[number] += 1

    for number in range(0, 11):
        percentage = (slownik[number] / 10000) * 100
        slownik[number] = round(float(percentage), 2)

    return slownik
