import random


def flip_coin() -> dict:
    list_res = []
    dict_of_res = {}
    for _ in range(10000):
        what_can_be = ["head", "not head"]
        one_of_circle = 0
        for _ in range(10):
            res_of_flip = random.choice(what_can_be)
            if res_of_flip == "head":
                one_of_circle += 1
        list_res.append(one_of_circle)

    for number in range(11):
        dict_of_res[number] = round((list_res.count(number) / 10000 * 100), 2)

    return dict_of_res
