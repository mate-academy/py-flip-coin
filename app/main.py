import random


def flip_coin() -> dict:
    result = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0,
              6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
    for iteration in range(10000):
        heads_counter = 0
        for i in range(10):
            if random.choice(["Heads", "Tails"]) == "Heads":
                heads_counter += 1
        result[heads_counter] += 1

    return {key: result[key] / 100 for key in result}
