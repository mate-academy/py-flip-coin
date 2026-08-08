from random import choice


def flip_coin() -> dict:
    experiments_count = 10000
    times_flipped = 10

    statistics = {i: 0 for i in range(times_flipped + 1)}

    for _ in range(experiments_count):
        flips = [choice((0, 1)) for _ in range(times_flipped)]

        count_heads = flips.count(0)
        statistics[count_heads] += 1

    for key in statistics:
        statistics[key] /= experiments_count
        statistics[key] *= 100

    return statistics


print(flip_coin())
