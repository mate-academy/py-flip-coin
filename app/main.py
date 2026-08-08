import random


def flip_coin() -> None:
    result = {i: 0 for i in range(11)}

    for attempt in range(10000):
        number_of_heads = 0

        for flip in range(10):
            flip_result = random.randint(0, 1)  # 1 = orzeł, 0 = reszka
            number_of_heads += flip_result

        result[number_of_heads] += 1

    for key in result:
        result[key] = (result[key] / 10000) * 100

    return result
