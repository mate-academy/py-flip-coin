import random


def flip_coin(
        n_experiments: int = 10000,
        n_flips: int = 10
) -> dict[int, float]:

    experiments_dict = {}
    sum_of_heads = 0
    for i in range(0, n_flips + 1):
        experiments_dict[i] = 0
    for experiment in range(n_experiments):
        for flip in range(n_flips):
            # if experiment == n_experiments - 1:
            #     breakpoint()
            coin_flip = random.randint(0, 1)
            if coin_flip == 1:
                sum_of_heads += coin_flip
        experiments_dict[sum_of_heads] += 1
        sum_of_heads = 0

    for i in range(0, n_flips + 1):
        experiments_dict[i] = (experiments_dict[i] / n_experiments) * 100

    return experiments_dict


flip_coin()
