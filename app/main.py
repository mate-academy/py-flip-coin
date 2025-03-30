from random import randint


def flip_coin() -> dict:
    result = {

    }

    for i in range(11):
        result[i] = 0

    for _ in range(10000):
        coin_eagle = 0
        for i in range(10):
            eagle = randint(0, 1)

            if eagle:
                coin_eagle += 1

        result[coin_eagle] += 1

    for i in range(0, 11):
        result[i] = round(result[i] / 100, 2)

    return result


flip_coin()
