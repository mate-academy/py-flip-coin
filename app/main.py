from random import choices


def flip_coin() -> dict:
    options = ["heads", "tails"]
    heads = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
    for _ in range(10001):
        case = choices(options, k=10)
        heads[case.count("heads")] += 1

    return {key: round((value / 10000) * 100, 2)
            for key, value in heads.items()}
