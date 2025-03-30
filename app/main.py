import random


def flip_coin() -> dict:
    data = {str(i): 0 for i in range(11)}
    sides = ["head", "tail"]
    for _ in range(10000):
        number_of_heads = 0
        for _ in range(10):
            if random.choice(sides) == "head":
                number_of_heads += 1
        print(number_of_heads)
        data[str(number_of_heads)] += 1
    percentages = {
        i: round((data[str(i)] / 10000) * 100, 2)
        for i in range(11)
    }
    return percentages
