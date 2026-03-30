import random


def flip_coin() -> dict:
    result = {num: 0 for num in range(11)}

    for num1 in range(10000):
        count = 0
        for num2 in range(10):
            if random.choice(["heads", "tails"]) == "heads":
                count += 1
        result[count] += 1

    percent_result = {key: value / 100 for key, value in result.items()}
    print(percent_result)
    return percent_result
