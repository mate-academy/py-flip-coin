import random


def flip_coin() -> dict:
    result = {}
    flip = ["head", "other"]
    for _ in range(10000):
        case_result = []
        for _ in range(10):
            case_result.append(random.choice(flip))
        if case_result.count("head") in result:
            result[case_result.count("head")] += 1
        else:
            result[case_result.count("head")] = 1
    for each in result:
        result[each] /= 100

    return result
