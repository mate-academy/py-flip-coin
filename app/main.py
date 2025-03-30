from random import randint


def flip_coin() -> dict:
    result = {i: 0 for i in range(11)}

    for case in range(10000):
        case_res = 0
        for toss in range(10):
            case_res += randint(0, 1)
        result[case_res] += 1

    return {
        key: (value / 10000 * 100)
        for key, value in result.items()
    }
