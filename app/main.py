import random


def flip_coin():
    count = 0
    final_dict = {i: 0 for i in range(11)}
    list_ = ["heads", "tails"]
    for i in range(10000):
        for i in range(10):
            item = random.choice(list_)
            if item == "heads":
                count += 1
        final_dict[count] += 0.01
        count = 0
    for i in range(11):
        rounded_number = round(final_dict[i], 2)
        final_dict[i] = rounded_number
    return final_dict
