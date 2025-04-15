import random


def flip_coin() -> None:
    dictionary = {i: 0 for i in range(11)}
    for _ in range(1000):
        head = 0
        for _ in range(10):
            coin = random.choice(["head", "tail"])
            if coin == "head":
                head += 1
        dictionary[head] += 1

    dictionary2 = {key: round(value / 10, 2) for key, value in
                   dictionary.items()}
    print(dictionary2)
    return dictionary2
