import random


def flip_coin() -> dict:
    result_dict = {i: 0 for i in range(11)}

    for _ in range(10000):
        counter = 0
        for i in range(10):
            if random.choice(("heads", "tails")) == "heads":
                counter += 1
        result_dict[counter] += 1
    return {key: (value / 100) for key, value in result_dict.items()}
