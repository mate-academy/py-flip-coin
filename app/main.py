import random


def flip_coin() -> dict:
    result = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0,
              6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
    for _ in range(10000):
        num_of_coins = []
        for _ in range(10):
            coin = random.randint(0, 1)
            if coin == 1:
                num_of_coins.append(1)
            else:
                continue
        count_of_coins = sum(num_of_coins)
        if count_of_coins in result.keys():
            result[count_of_coins] += 1
    for key in result.keys():
        result[key] = round(result[key] / 100, 2)
    return result
