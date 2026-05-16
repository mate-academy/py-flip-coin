from random import randint


def flip_coin() -> dict:
    output_dict = {}
    total_flips = 0

    for _ in range(10000):
        heads = 0
        for _ in range(10):
            if randint(0, 1) == 1:
                heads += 1
        output_dict[heads] = output_dict.get(heads, 0) + 1
        total_flips += 1

    percentages = {}
    for heads, count in output_dict.items():
        percentages[heads] = (count / total_flips) * 100

    return percentages
