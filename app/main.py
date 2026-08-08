import random


def flip_coin() -> dict:
    list_to_analyze = []
    for toss in range(10000):
        heads_side = 0
        for flip in range(10):
            flip_result = random.choice(
                ["head", "tail"]
            )
            if flip_result == "head":
                heads_side += 1
        list_to_analyze.append(heads_side)

    final_dict = {}
    for result in set(list_to_analyze):
        final_dict[result] = list_to_analyze.count(result) / 100
    return final_dict
