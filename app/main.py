import random


def flip_coin() -> dict:
    unsorted_dict = {}
    iterations = 10000

    for _ in range(iterations):
        heads_counter = 0

        for _ in range(10):

            drop = random.choice(["heads", "tails"])
            if drop == "heads":
                heads_counter += 1

        unsorted_dict[heads_counter] = unsorted_dict.get(heads_counter, 0) + 1

    sorted_dict = {key: unsorted_dict[key] for key in sorted(unsorted_dict)}
    for key, value in sorted_dict.items():
        sorted_dict[key] = round((value / iterations * 100), 2)
    return sorted_dict
