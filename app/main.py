import random


def flip_coin() -> dict:
    result_dict = {}
    result = []
    orel = []

    for i in range(10000):
        for poput in range(10):
            result.append(random.randint(0, 1))
        else:
            orel.append(result.count(1))
            result = []

    for i in range(0, 11):
        result_dict[i] = round((orel.count(i) / len(orel)) * 100, 2)

    return result_dict


# def draw_gaussian_distribution_graph() -> None:
#     pass


print(flip_coin())
