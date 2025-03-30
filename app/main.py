from random import choice


def flip_coin() -> dict:
    variant = ["head", "coin"]
    possible_count_times = {i: 0 for i in range(0, 11)}

    for _ in range(10000):
        count = 0
        for i in range(10):
            if choice(variant) == "head":
                count += 1
        possible_count_times[count] += 1
    result = {i: round(possible_count_times[i] / 100, 2)
              for i in possible_count_times.keys()}
    return result
