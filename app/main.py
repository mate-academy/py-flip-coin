import random


def flip_coin(num_of_try: int = 10000) -> dict:
    counts_dict = {count: 0 for count in range(11)}
    for num in range(num_of_try):
        heads = 0
        for ran in range(10):
            if random.random() < 0.5:
                heads += 1
        counts_dict[heads] += 1
    total_trials = sum(counts_dict.values())
    percent = {}
    for key in counts_dict:
        percent[key] = (100 * counts_dict[key] / total_trials)
    return percent
