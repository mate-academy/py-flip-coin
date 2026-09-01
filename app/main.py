import random


def flip_coin() -> dict:
    predict = {key: 0 for key in range(11)}

    for _ in range(10000):
        number_of_tail = 0
        for chance in range(10):
            if random.choice(["head", "tail"]) == "tail":
                number_of_tail += 1
        predict[number_of_tail] += 1
    return {key: round((value / sum(predict.values()) * 100), 2)
            for key, value in predict.items()}
