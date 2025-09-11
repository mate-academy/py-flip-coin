from random import choice


def get_one_flipping_experiment_result() -> int:
    result = 0
    for i in range(10):
        if choice(["Heads", "Tails"]) == "Heads":
            result += 1
    return result


def experiment() -> dict:
    result = dict({i: 0 for i in range(11)})
    for _ in range(10_000):
        num = get_one_flipping_experiment_result()
        result[num] = result[num] + 1
    return result


def flip_coin() -> dict:
    result_dict = experiment()
    for key, value in result_dict.items():
        result_dict[key] = round(value / 100, 2)
    return result_dict
