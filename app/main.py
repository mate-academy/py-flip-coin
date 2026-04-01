import random


def flip_coin() -> dict:
    result_dict = {}
    list_of_counts = []
    result_dict_with_percentage = {}

    for _ in range(10000):
        heads_count = 0
        for _ in range(10):
            side = random.choice(["Head", "Tail"])
            if side == "Head":
                heads_count += 1

        list_of_counts.append(heads_count)

    for _ in list_of_counts:
        if _ not in result_dict:
            result_dict[_] = 1
        result_dict[_] += 1

    for key in result_dict:
        percent = round(result_dict[key] / 10000 * 100, 2)
        result_dict_with_percentage[key] = percent

    return result_dict_with_percentage
