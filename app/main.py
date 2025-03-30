from random import randint


def flip_coin() -> None:
    result_dict = {}
    result_dict_for_return = {}
    for ten_time_flip in range(10000 + 1):
        result_list = [randint(0, 1) for _ in range(1, 11)]
        if sum(result_list) in result_dict:
            result_dict[sum(result_list)] += 1
        else:
            result_dict[sum(result_list)] = 1
    for i in range(0, 11):
        result_dict_for_return[i] = round((result_dict[i] / 10000), 4) * 100
    return result_dict_for_return
