import random


def flip_coin() -> dict:
    result_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0,
                   6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
    flip_times = 10000
    for _ in range(flip_times):
        head_count = 0
        for i in range(10):
            if random.choice(["head", "tail"]) == "head":
                head_count += 1
        result_dict[head_count] += 1
    return {num: round((quantity / flip_times) * 100, 2)
            for num, quantity in result_dict.items()}
