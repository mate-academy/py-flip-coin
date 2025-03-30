import random


def flip_coin() -> dict:
    num_simulations = 10000
    number_of_flips = 10
    result = {i: 0 for i in range(number_of_flips + 1)}

    for _ in range(num_simulations):
        heads_count = sum(random.randint(0, 1) for _ in range(number_of_flips))
        result[heads_count] += 1

    result_percentage = {k: (v / num_simulations)
                         * 100 for k, v in result.items()}
    return result_percentage
