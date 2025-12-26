import random

def flip_coin() -> dict:
    result = {}
    for i in range(10000):
        ten_flips = 0
        for _ in range(10):
            coin_flip = random.randint(0, 1)
            if coin_flip == 1:
                ten_flips += 1
        result[i] = ten_flips / 10
    print(result)
    return result

flip_coin()