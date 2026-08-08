# write your code here
import random


def flip_coin() -> dict:
    coin = ["head", "tail"]
    probability = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0,
                   8: 0, 9: 0, 10: 0}
    for _ in range(10000):
        result = 0
        for _ in range(10):
            if random.choice(coin) == "head":
                result += 1
        probability[result] += 1
    for key in probability.keys():
        probability[key] /= 100
    return probability
